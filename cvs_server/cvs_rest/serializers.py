from rest_framework import serializers
from cvs_rest.models import *

"""
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = ('id', 'name', 'image', 'price', 'flag', 'manufacturer', 'review_set', 'comment_set')
"""

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
       fields = ('id', 'created', 'edited', 'title', 'user_id', 'product_id')



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

#Comment - Rating은 1:1 연결
#Rating과 Comment모두 수정 가능 
class CommentSerializer(serializers.ModelSerializer) :

    rating = RatingSerializer()

    def create(self, validated_data) :
        rating_data = validated_data.pop('rating')
        comment = Comment.objects.create(**validated_data)
        rating_data['comment']=comment
        Rating.objects.create(**rating_data)
        return comment

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
    
    class Meta:
        model = Comment
        fields = ('id', 'created', 'edited', 'content', 'user_id', 'product', 'rating')

class ProductDetailSerializer(serializers.ModelSerializer) :
    comments = serializers.PrimaryKeyRelatedField(many=True, allow_null=True, queryset=Comment)
    class Meta:
        model = Product
        fields = ('name', 'image', 'price', 'manufacturer', 'PB', 'large_category', 'small_category', 'comments')

class ProductSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Product
        fields = '__all__'

class PostRelatedField(serializers.RelatedField) :

    created = serializers.DateTimeField()
    image = serializers.ImageField()
    content = serializers.CharField()
    
    
    def to_representation(self, value) :
        if isinstance(value, Review) :
            return 'review_id: ' + value.id
        elif isinstance(value, Recipe) :
            return 'recipe_id: ' + value.id
        raise Exception('Unexpected type of Post object')


"""
class CommentRelatedField(serializers.RelatedField) :
    def to_native(self, value):
        if isinstance(value, Product):
            serializer = ProductSerializer(value)
        elif isinstance(value, Recipe) :
            serializer = RecipeSerializer(value)
        else :
            raise Exception('Unexpected type of comment object')
        return serializer.data
class CommentIdSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Product
        fields = ('id')

class ReviewIdSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Review
        fields = ('id')
"""



"""
class RatingObjectRelatedField(serializers.RelatedField) :

    def to_native(self, value) :
        #ratingValue = 

    def to_native(self, value) :
        if isinstance(value, models.Comment) :
            serializer = CommentSerializer(value)
        elif isinstance(value, models.Review) :
            serializer = ReviewSerializer(value)
        else :
            raise Exception('Unexpected type of comment object')
        return serializer.data


class PostSerializer(serializers.ModelSerializer) :
    #something"""
