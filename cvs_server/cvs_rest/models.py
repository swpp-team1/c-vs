from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import fields
from django.db.models import Avg   

class ProductManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().annotate(rating_avg=Avg('rating__value'))

class Product(models.Model):
    DEFAULT_PK = 1
    name = models.CharField(max_length=100)
    image = models.URLField()
    price = models.IntegerField()
    SEVEN_ELEVEN = 'SE'
    GS25 = 'GS'
    CU = 'CU'
    MANUFACTURER_CHOICES = (
        (SEVEN_ELEVEN, 'Seven Eleven'),
        (GS25, 'GS25'),
        (CU, 'CU'),
    )
    manufacturer = models.CharField(
        max_length=10
    )
    PB = models.BooleanField()
    #comments = fields.GenericRelation('Comment', related_query_name='products')
    #reviews = fields.GenericRelation('Review', related_query_name='products') 

    large_category = models.CharField(
        max_length=10,
        null=True,
    )
    small_category = models.CharField(
        max_length=10,
        null=True,
    )
    # overide default manager
    objects = ProductManager()

    class Meta:
        ordering = ('manufacturer', 'name',)


class CustomUser(AbstractUser):
    created = models.DateTimeField(auto_now_add=True)


class Recipe(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=100, null=False)
    #ingredients = models.TextField()
    ingredients = models.ManyToManyField('Product')
    user_id = models.ForeignKey(
        'CustomUser',
        on_delete=models.CASCADE,
    )
    post = fields.GenericRelation('Post', related_query_name='recipe') 
    

    class Meta:
        ordering = ('created',)


class Review(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=100)
    rating = fields.GenericRelation('Rating', related_query_name='review')
    user_id = models.ForeignKey(
        'CustomUser',
        on_delete=models.CASCADE,
    )
    
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    post = fields.GenericRelation('Post', related_query_name='review', null=True)    
    
    class Meta:
        ordering = ('created',)

    

class Comment(models.Model):
    DEFAULT_PK = 1
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    content = models.TextField()
    rating = fields.GenericRelation('Rating')
    user_id = models.ForeignKey(
        'CustomUser',
        on_delete=models.CASCADE,
    )
    product = models.ForeignKey('Product', on_delete=models.CASCADE, default=Product.DEFAULT_PK)
    

    class Meta:
        ordering = ('created',)

#save review images in "media/review"
#and save recipe images in "media/recipe"
def image_directory_path(instance, filename) :
    if instance.content_type.name == 'review' :
        parent = 'review'
    elif instance.content_type.name == 'recipe' :
        parent = 'recipe'
    return '{0}/{1}'.format(parent, filename)


class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, upload_to=image_directory_path, default = 'test.jpg', max_length=1000)
    content = models.TextField(null=True)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    belong_to = fields.GenericForeignKey('content_type', 'object_id')
    
    class Meta:
        ordering = ('created',)





class Rating(models.Model) :
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    value = models.PositiveSmallIntegerField(null=False)
    
    user_id = models.ForeignKey(
        'CustomUser',
        related_name='ratings',
        on_delete=models.CASCADE,
    )
    
    product = models.ForeignKey(
        'Product',
        on_delete=models.CASCADE,     
    )
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    belong_to = fields.GenericForeignKey('content_type', 'object_id')

    class Meta:
        ordering = ('created',)

