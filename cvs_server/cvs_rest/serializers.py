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

class RatingSerializer(serializers.ModelSerializer) :

    #override
    def create(self, validated_data) :
        return Rating.objects.create(**validated_data)
    
    #override
    def update(self, instance, validated_data) :
        instance.edited = validated_data.get('edited', instance.edited)
        instance.value = validated_data.get('value', instance.value)
        instance.save()
        return instance
    
    
    class Meta:
        model = Rating
        fields = ('id', 'created', 'edited', 'value', 'user_id', 'comment')

class CommentSerializer(serializers.ModelSerializer) :

    rating = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ('id', 'created', 'edited', 'content', 'user_id', 'product', 'rating')
    
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
    class Meta :
        model = Post
        fields = ('created', 'image', 'content')

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
        fields = ('created', 'edited', 'title', 'user_id', 'product', 'post', 'rating')
    
    def get_rating(self, obj) :
        rat = obj.rating.get()
        if rat :
            return rat.value
        return 0

