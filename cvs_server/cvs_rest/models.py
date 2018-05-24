from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import fields


class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.URLField()
    price = models.IntegerField()
    flag = models.CharField(max_length=50)
    SEVEN_ELEVEN = 'SE'
    GS25 = 'GS'
    CU = 'CU'
    MANUFACTURER_CHOICES = (
        (SEVEN_ELEVEN, 'Seven Eleven'),
        (GS25, 'GS25'),
        (CU, 'CU'),
    )
    manufacturer = models.CharField(
        max_length=2,
        choices=MANUFACTURER_CHOICES,
    )
    PB = models.BooleanField()
    comments = fields.GenericRelation('Comment', related_query_name='products')
    reviews = fields.GenericRelation('Review', related_query_name='products')
    ratings = fields.GenericRelation('Rating', related_query_name='products')


    class Meta:
        ordering = ('manufacturer', 'name',)

class CustomUser(AbstractUser):
    created = models.DateTimeField(auto_now_add=True)


class Recipe(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=100) 
    ingredients = models.ManyToManyField('Product')
    user_id = models.ForeignKey(
        'CustomUser',
        on_delete=models.CASCADE,
    )
    images = fields.GenericRelation('Post', related_query_name='recipes') 
    comments = fields.GenericRelation('Comment', related_query_name='recipes')
    reviews = fields.GenericRelation('Review', related_query_name='recipes')
    ratings = fields.GenericRelation('Rating', related_query_name='recipes')


    class Meta:
        ordering = ('created',)

class Rating(models.Model) :
    created = models.DateTimeField(auto_now_add=True)
    value = models.PositiveSmallIntegerField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    belong_to = fields.GenericForeignKey('content_type', 'object_id')

    class Meta:
        ordering = ('created',)


class Review(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=100)
    user_id = models.ForeignKey(
        'CustomUser',
        on_delete=models.CASCADE,
    )
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    belong_to = fields.GenericForeignKey('content_type', 'object_id') 
    images = fields.GenericRelation('Post', related_query_name='reviews')
    rating = fields.GenericRelation('Rating', related_query_name='reviews')


    class Meta:
        ordering = ('created',)


class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    content = models.TextField()
    #rating = models.PositiveSmallIntegerField()
    rating = fields.GenericRelation('Rating', related_query_name='comments')
    user_id = models.ForeignKey(
        'CustomUser',
        on_delete=models.CASCADE,
    )
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    belong_to = fields.GenericForeignKey('content_type', 'object_id')


    class Meta:
        ordering = ('created',)


class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField()
    content = models.TextField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    belong_to = fields.GenericForeignKey('content_type', 'object_id')
    

    class Meta:
        ordering = ('created',)
