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
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    search_fields = ('name',)
    filter_fields = ('price', 'large_category', 'small_category', 'manufacturer', 'PB')

#/products/id
class ProductDetail(generics.RetrieveAPIView) :
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer



#일단 유저빼고 해봄
@api_view(['POST'])
@permission_classes((IsAuthenticatedOrReadOnly,))
def create_comment(request, format=None) :

    #create and save new rating object
    data = request.data
    rating = data.get('rating')
    content = data.get('content')
    product = data.get('product')
        
    if not (rating and content and product):
        return Response(data={'message':'content or product or rating Field does not exist'}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        product_obj = Product.objects.get(id=product)
    except ObjectDoesNotExist:    
        return Response(data={'message':'Wrong Product ID'}, status=status.HTTP_400_BAD_REQUEST)
   
    comment_obj = Comment.objects.create(content=content, product=product_obj, user_id=request.user)
    Rating.objects.create(comment=comment_obj, value=rating, user_id=request.user)
    
    serializer = CommentSerializer(comment_obj) 
    #if serializer.is_valid():
        #serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)



@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((IsAuthenticatedOrReadOnly,))
def comment_detail(request, pk, format=None) :
    try:
        comment = Comment.objects.get(pk=pk)
    except Comment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET' :
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    
    elif comment.user_id != request.user :
        return Response(data={'message':'You are not owner'}, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PUT' :
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE' :
        comment.delete()
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
        serializer = ReviewListSerializer(reviews, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST' :
        data = request.data
        title = data.get('title')
        product_id = data.get('product_id')

        #에러메세지 나중에 세분화할 것 
        if not (title and product_id) :
            return Response(data={'message':'title or rating Field does not exist'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            product_obj = Product.objects.get(id=product_id)
        except ObjectDoesNotExist :
            return Response(data={'message':'Wrong Product ID'}, status=status.HTTP_400_BAD_REQUEST)
        
        review_obj = Review.objects.create(title=title, user_id=request.user, product_id=product_obj)
        Post.objects.create(belong_to=review_obj, image=data.get('image'), content=data.get('content'))
        serializer = ReviewDetailSerializer(review_obj)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)

#/reviews/pk
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((IsAuthenticatedOrReadOnly,))
def review_detail(request, pk, format=None) :
    try :
        review = Review.objects.get(pk=pk)
    except Review.DoesNotExist :
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET' :
        serializer = ReviewDetailSerializer(review)
        return Response(serializer.data)
    
    elif review.user_id != request.user :
        return Response(data={'message':'You are not owner'}, status=status.HTTP_400_BAD_REQUEST)
    

    #안됨 ㅜㅜ
    elif request.method == 'PUT' :
        data = request.data
        
        #create 해서 넣어주고 나서 delete?
        #deleted former post
        #post_to_delete = Post.objects.filter(review__id=pk)
        #post_to_delete.delete()

        new_post_image = data.get('image')
        new_post_content = data.get('content')

        Post.objects.create(belong_to=review, image=new_post_image, content=new_post_content)

        review.edited = data.get('edited')
        review.title = data.get('title')
        review.save()

        #in serializer, create new post object and update review object
        serializer = ReviewDetailSerializer(review, data=data)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE' :
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


##for check
class PostList(generics.ListAPIView) :
    queryset = Post.objects.all()
    serializer_class = PostSerializer


@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticatedOrReadOnly,))
def get_create_review(request, format=None) :
    if request.method == 'GET' :
        try :
            reviews = Review.objects.all()
        except Review.DoesNotExist:
            return Response(data={'message':'No reviews to show'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ReviewListSerializer(reviews, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST' :
        data = request.data
        title = data.get('title')
        product_id = data.get('product_id')

        #에러메세지 나중에 세분화할 것 
        if not (title and product_id) :
            return Response(data={'message':'title or rating Field does not exist'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            product_obj = Product.objects.get(id=product_id)
        except ObjectDoesNotExist :
            return Response(data={'message':'Wrong Product ID'}, status=status.HTTP_400_BAD_REQUEST)
        
        review_obj = Review.objects.create(title=title, user_id=request.user, product_id=product_obj)
        Post.objects.create(belong_to=review_obj, image=data.get('image'), content=data.get('content'))
        serializer = ReviewDetailSerializer(review_obj)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)


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
