from rest_framework import serializers
from cvs_rest.models import *
from django.db.models import Avg

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'created', 'email', 'comment_set', 'review_set')
        

class RecipeSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Recipe
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer) :

    rating = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ('id', 'created', 'edited', 'content', 'user_id', 'product', 'rating')
        depth = 1
    
    
    def get_rating(self, obj):
        rat = obj.rating.get()
        if rat:
            return rat.value
        return 0

class ProductDetailSerializer(serializers.ModelSerializer) :
    rating_avg = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('id', 'name', 'image', 'price', 'manufacturer', 'PB', 'large_category', 'small_category', 'rating_avg', 'comment_set', 'review_set')
    
    def get_rating_avg(self,obj):
        return obj.rating_avg or 0
    

class ProductSerializer(serializers.ModelSerializer) :
    
    rating_avg = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer) :

    image = serializers.ImageField()

    class Meta :
        model = Post
        fields = ('created', 'image', 'content')
        depth = 2

class ReviewListSerializer(serializers.ModelSerializer) :

    rating = serializers.SerializerMethodField()

    class Meta:
       model = Review
       fields = ('id', 'created', 'edited', 'title', 'user_id', 'product', 'rating')
    
    def get_rating(self, obj) :
        rat = obj.rating.get()
        if rat:
            return rat.value
        return 0

class ReviewDetailSerializer(serializers.ModelSerializer) :

    rating = serializers.SerializerMethodField()
    post = PostSerializer(many=True)

    class Meta :
        model = Review
        fields = ('id', 'created', 'edited', 'title', 'user_id', 'product', 'post', 'rating')
        depth = 1
    
    def get_rating(self, obj) :
        rat = obj.rating.get()
        if rat :
            return rat.value
        return 0


#this serializer is used only for testing
class RatingSerializer(serializers.ModelSerializer) :

    class Meta:
        model = Rating
        fields = ('id', 'created', 'edited', 'value', 'user_id', 'product', 'content_type', 'object_id')
        depth = 2
