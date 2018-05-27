from rest_framework import serializers
from cvs_rest.models import Product, CustomUser, Review, Recipe, Comment, Post


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'image', 'price', 'flag', 'manufacturer', 'review_set', 'comment_set')


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'nickname', 'created', 'email', 'recipe_set', 'review_set', 'comment_set')


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ('')
