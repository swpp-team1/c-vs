from cvs_rest.models import * 
from cvs_rest.serializers import *
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from rest_framework import status, generics, filters
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.contrib.contenttypes.models import ContentType
from django_filters.rest_framework import DjangoFilterBackend
from django.core.validators import validate_email
from django.core.exceptions import ValidationError, ObjectDoesNotExist
import re

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data.get('user')
        token, created = Token.objects.get_or_create(user=user)
        response_json = UserSerializer(user).data
        response_json['token'] = token.key
        return Response(response_json)



@api_view(['POST'])
def sign_up(request):
    
    data = request.data
    name = data.get('username')
    password = data.get('password')
    email = data.get('email')
    name_regex = re.compile(r'^[A-Za-z]{1}[A-Za-z0-9_]{3,19}$') 
    
    if not (name and password and email):
        return Response(data={'message':'username or password or email field is missing.'}, status=status.HTTP_400_BAD_REQUEST)
    
    if not name_regex.match(name):
        return Response(data={'message':'username is at least 4 to 20 only with alaphabet, number and under score'}, status=status.HTTP_400_BAD_REQUEST)
    
    if email :
        try:
            validate_email(email)
        except ValidationError:
            return Response(data={'message':'email is not validated.'}, status=status.HTTP_400_BAD_REQUEST) 

    if CustomUser.objects.filter(username=name):
        return Response(data={'message':'User name aleady exists.'}, status=status.HTTP_400_BAD_REQUEST)
            
    if len(password) < 6:
        return Response(data={'message':'Password should be at least 6.'}, status=status.HTTP_400_BAD_REQUEST)
        
    user, created = CustomUser.objects.get_or_create(username=name, email=email)
    if created:
        user.set_password(password)
        token, created = Token.objects.get_or_create(user=user)
        response_json = UserSerializer(user).data
        response_json['token'] = token.key
        user.save()
        return Response(response_json, status=status.HTTP_201_CREATED)
    else:
        return Response(data={'message':'User already exist'}, status=status.HTTP_400_BAD_REQUEST)

#/users
class CustomUserList(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

#/users/id
class CustomUserDetail(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

#/products
class ProductList(generics.ListAPIView) :
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter)
    search_fields = ('name',)
    ordering_fields = ('name', 'rating_avg')
    filter_fields = ('price', 'large_category', 'small_category', 'manufacturer', 'PB')

#/products/id
class ProductDetail(generics.RetrieveAPIView) :
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer


#/comments/
@api_view(['GET','POST'])
@permission_classes((IsAuthenticatedOrReadOnly,))
def create_comment(request, format=None) :

    if request.method == 'GET':
        comments = Comment.objects.all()
        product = request.query_params.get('product', None)
        user_id = request.query_params.get('user_id', None)
        if product is not None:
            comments = comments.filter(product=product)
        if user_id is not None:
            comments = comments.filter(user_id=user_id)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        #create and save new rating object
        data = request.data
        rating = data.get('rating')
        content = data.get('content')
        product = data.get('product')
        
        if not (rating and content and product):
            return Response(data={'message':'content or product or rating Field is not existed'}, status=status.HTTP_400_BAD_REQUEST)
        
        rating = int(rating)
        
        if rating < 1 or rating > 5:
            return Response(data={'message':'rating should be 1 to 5'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            product_obj = Product.objects.get(id=product)
        except ObjectDoesNotExist:    
            return Response(data={'message':'Wrong Product ID'}, status=status.HTTP_400_BAD_REQUEST)
   
        comment_obj = Comment.objects.create(content=content, product=product_obj, user_id=request.user)
        Rating.objects.create(belong_to=comment_obj, value=rating, user_id=request.user, product=product_obj)
    
        serializer = CommentSerializer(comment_obj) 
        return Response(serializer.data, status=status.HTTP_201_CREATED)


#/comments/pk/
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((IsAuthenticatedOrReadOnly,))
def comment_detail(request, pk, format=None) :
    try:
        comment_obj = Comment.objects.get(pk=pk)
    except Comment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET' :
        serializer = CommentSerializer(comment_obj)
        return Response(serializer.data)
    
    elif comment_obj.user_id != request.user :
        return Response(data={'message':'You are not owner'}, status=status.HTTP_400_BAD_REQUEST)


    elif request.method == 'PUT' :

        data = request.data
        new_value = data.get('rating')
        comment_type = ContentType.objects.get_for_model(comment_obj)
        
        try :
            rating_obj = Rating.objects.get(content_type__pk=comment_type.id, object_id=comment_obj.id)
        except Rating.DoesNotExist :
            return Response(status=status.HTTP_404_NOT_FOUND)
        rating_obj.value = new_value
        rating_obj.save()

        serializer = CommentSerializer(comment_obj, data=data)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE' :
        comment_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    

#/reviews/
@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticatedOrReadOnly,))
def get_create_review(request, format=None) :

    if request.method == 'GET' :
        try :
            reviews = Review.objects.all()
        except Review.DoesNotExist:
            return Response(data={'message':'No reviews to show'}, status=status.HTTP_404_NOT_FOUND)
        
        product = request.query_params.get('product', None)
        user_id = request.query_params.get('user_id', None)
        if product is not None :
            reviews = reviews.filter(product=product)
        if user_id is not None :
            reviews = reviews.filter(user_id=user_id)
        serializer = ReviewListSerializer(reviews, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST' :
        data = request.data
        rating = data.get('rating')
        title = data.get('title')
        product = data.get('product')

        #에러메세지 나중에 세분화할 것 
        if not (title and product and rating) :
            return Response(data={'message':'title or product or rating does not exist'}, status=status.HTTP_400_BAD_REQUEST)
        
        rating = int(rating)

        if rating < 1 or rating > 5:
            return Response(data={'message':'rating should be 1 to 5'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            product_obj = Product.objects.get(id=product)
        except ObjectDoesNotExist :
            return Response(data={'message':'Wrong Product ID'}, status=status.HTTP_400_BAD_REQUEST)
        
        review_obj = Review.objects.create(title=title, user_id=request.user, product=product_obj)
        Rating.objects.create(belong_to=review_obj, value=rating, user_id=request.user, product=product_obj)
        Post.objects.create(belong_to=review_obj, image=data.get('image'), content=data.get('content'))
        serializer = ReviewDetailSerializer(review_obj)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)

#/reviews/pk/
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((IsAuthenticatedOrReadOnly,))
def review_detail(request, pk, format=None) :
    try :
        review_obj = Review.objects.get(pk=pk)
    except Review.DoesNotExist :
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET' :
        serializer = ReviewDetailSerializer(review_obj)
        return Response(serializer.data)
    
    elif review_obj.user_id != request.user :
        return Response(data={'message':'You are not owner'}, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PUT' :
        data = request.data

        #delete former post
        review_type = ContentType.objects.get_for_model(review_obj)
        try :
            post_to_delete = Post.objects.get(content_type__pk=review_type.id, object_id=review_obj.id)
        except Post.DoesNotExist :
            return Response(status=status.HTTP_404_NOT_FOUND)
        post_to_delete.delete()

        #create new post
        post_obj = Post(belong_to=review_obj)
        if data.get('image') :
            post_obj.image = data.get('image')
        if data.get('content') :
            post_obj.content = data.get('content')
        post_obj.save()
        
        #edit rating value of nested Rating object
        if data.get('rating') :
            try :
                rating_obj = Rating.objects.get(content_type__pk=review_type.id, object_id=review_obj.id)
            except Rating.DoesNotExist :
                return Response(status=status.HTTP_404_NOT_FOUND)
            rating_obj.value = data.get('rating')
            rating_obj.save()
        
        #edit title of Review object
        if data.get('title') :
            review_obj.title = data.get('title')
            review_obj.save()

        serializer = ReviewDetailSerializer(review_obj)
        return Response(serializer.data)
    
    elif request.method == 'DELETE' :
        review_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


##for check
class PostList(generics.ListAPIView) :
    queryset = Post.objects.all()
    serializer_class = PostSerializer


"""



#/recipes
class RecipeList(generics.ListCreateAPIView) :
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('user_id',)


#/recipes/pk
class RecipeDetail(generics.RetrieveUpdateDestroyAPIView) :
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

"""
