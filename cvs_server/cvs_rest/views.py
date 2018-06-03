from cvs_rest.models import * 
from cvs_rest.serializers import *
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status, generics, filters
from rest_framework.decorators import api_view
from django_filters.rest_framework import DjangoFilterBackend
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
import re

class CustomAuthToken(ObtainAuthToken):
    def post(self, request,*args, **kwargs):
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
        
    user, created = CustomUser.objects.get_or_create(username=name)
    if created:
        user.set_password(password)
        user['email'] = email
        token, created = Token.objects.get_or_create(user=user)
        response_json = UserSerializer(user).data
        response_json['token'] = token.key
        user.save()
        return Response(response_json, status=status.HTTP_201_CREATED)
    else:
        return Response(data={'message':'User already exist'}, status=status.HTTP_400_BAD_REQUEST)


#/products
class ProductList(generics.ListAPIView) :
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    search_fields = ('name',)
    filter_fields = ('price', 'large_category', 'small_category', 'manufacturer', 'PB')


#/products/pk
class ProductDetail(generics.RetrieveAPIView) :
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


#/reviews
class ReviewList(generics.ListCreateAPIView) :
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('user_id',)


#/reviews/pk
class ReviewDetail(generics.RetrieveUpdateDestroyAPIView) :
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


"""
#review filtered by user
class ReviewListByUser(generics.ListAPIView) :
    serializer_class = ReviewSerializer

    def get_queryset(self) :
        user = self.request.user
        return Review.objects.filter(user_id=user)
"""


#/comments
class CommentList(generics.ListCreateAPIView) :
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('user_id',)


#/comments/pk
class CommentDetail(generics.RetrieveUpdateDestroyAPIView) :
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


#/users/pk
class CustomUserDetail(generics.RetrieveAPIView) :
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


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

