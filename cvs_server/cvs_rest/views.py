from django.http import Http404
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

import django_filters.rest_framework

from cvs_rest.models import *
from cvs_rest.serializers import *

"""
class ProductList(APIView) :
    def get(self, request, format=None) :
        all_products = Product.objects.all()
        serializer = ProductSerializer(all_products, many=True)
        return Response(serializer.data)
"""

#/products
class ProductList(generics.ListAPIView) :
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('manufacturer', 'PB')
"""
class ProductDetail(APIView) :
    def get_object(self, pk) :
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist :
            raise Http404
    
    def get(self, request, pk, format=None) :
        product = self.get_object(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
"""

#/products/pk
class ProductDetail(generics.RetrieveAPIView) :
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


#/reviews
class ReviewList(generics.ListCreateAPIView) :
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('user_id')

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
    filter_fields = ('user_id')


#/comments/pk
class CommentDetail(generics.RetrieveUpdateDestroyAPIView) :
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer



#/users/pk
class CustomUserDetail(generics.RetrieveAPIView) :
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


#/recipes
class RecipeList(generics.ListCreateAPIView) :
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('user_id')

#/recipes/pk
class RecipeDetail(generics.RetrieveUpdateDestroyAPIView) :
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer



    
