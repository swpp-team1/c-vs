from rest_framework import serializers
from cvs_rest.models import *
from django.db.models import Avg

class UserSerializer(serializers.ModelSerializer):
    #recipe_set = serializers.PrimaryKeyRelatedField(many=True, queryset=Recipe.objects.all())
    #review_set = serializers.PrimaryKeyRelatedField(many=True, queryset=Review.objects.all())
    #comment_set = serializers.PrimaryKeyRelatedField(many=True, queryset=Comment.objects.all())
    
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'created', 'email', 'comment_set')
        #fields = ('id', 'username', 'nickname', 'created', 'email', 'recipe_set', 'review_set', 'comment_set')


class RecipeSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Recipe
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer) :
   class Meta:
       model = Review
       fields = ('id', 'created', 'edited', 'title', 'user_id', 'product')

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

    #rating = RatingSerializer()
    rating = serializers.SerializerMethodField()
    '''
    def update(self, instance, validated_data) :

        rating_data = validated_data.pop('rating')
        rating = instance.rating
        instance.edited = validated_data.get('edited', instance.edited)
        instance.content = validated_data.get('content', instance.content)
        instance.save()
        
        rating.edited = rating_data.get('edited', rating.edited)
        rating.value = rating_data.get('value', raing.value)
        rating.save()
        return instance
    '''    
    class Meta:
        model = Comment
        fields = ('id', 'created', 'edited', 'content', 'user_id', 'product', 'rating')
    
    def get_rating(self, obj):
        rat = obj.rating.get()
        if rat:
            return rat.value
        return 0

class ProductDetailSerializer(serializers.ModelSerializer) :
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('id', 'name', 'image', 'price', 'manufacturer', 'PB', 'large_category', 'small_category', 'rating', 'comment_set')
    
    def get_rating(self,obj):
        ratings = Rating.objects.filter(product=obj)
        return ratings.aggregate(Avg('value'))['value__avg'] or 0
    

class ProductSerializer(serializers.ModelSerializer) :
    
    rating = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = ('id', 'name', 'image', 'price', 'manufacturer', 'PB', 'large_category', 'small_category', 'rating')
    
    def get_rating(self,obj):
        ratings = Rating.objects.filter(product=obj)
        return ratings.aggregate(Avg('value'))['value__avg'] or 0
        


