from rest_framework import serializers
import cvs_rest.models as models

class ProductSerializer(serializers.ModelSerializer) :
    class Meta:
        model = models.Product
        fields = '__all__'

class CustomUserSerializer(serializers.ModelSerializer) :
    class Meta:
        model = models.CustomUser
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer) :
   class Meta:
       model = models.Review
       fields = '__all__'

class CommentSerializer(serializers.ModelSerializer) :
    class Meta:
        model = models.Comment
        fields = '__all__'

class RecipeSerializer(serializers.ModelSerializer) :
    class Meta:
        model = models.Recipe
        fields = '__all__'