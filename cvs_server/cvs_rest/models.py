from django.db import models
from django.contrib.auth.models import AbstractUser


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

    class Meta:
        ordering = ('manufacturer', 'name',)

class CustomUser(AbstractUser):
    created = models.DateTimeField(auto_now_add=True)


class Recipe(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    ingredients = models.ManyToManyField('Product')
    user_id = models.ForeignKey(
        'CustomUser',
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ('created',)

class Review(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    user_id = models.ForeignKey(
        'CustomUser',
        on_delete=models.CASCADE,
    )
    product_id = models.ForeignKey(
        'Product',
        on_delete=models.CASCADE,
    )
    recipe_id = models.ForeignKey(
        'Recipe',
        on_delete=models.CASCADE,
    )

class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    content = models.TextField()
    rating = models.PositiveSmallIntegerField()
    user_id = models.ForeignKey(
        'CustomUser',
        on_delete=models.CASCADE,
    )
    product_id = models.ForeignKey(
        'Product',
        on_delete=models.CASCADE,
    )
    recipe_id = models.ForeignKey(
        'Recipe',
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ('created',)

class Image(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField()
    review_id = models.ForeignKey(
        'Review',
        on_delete=models.CASCADE,
    )
    recipe_id = models.ForeignKey(
        'Recipe',
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ('created',)
