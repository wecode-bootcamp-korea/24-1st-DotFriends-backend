from django.db import models

from users.models import User

class Product(models.Model):
    name             = models.CharField(max_length=64)
    price            = models.DecimalField(max_digits=10, decimal_places=3)
    discount_percent = models.DecimalField(max_digits=5, decimal_places=3,blank=True) 
    is_new           = models.BooleanField(default=False)
    category         = models.ForeignKey('category', on_delete=models.SET_NULL,null=True)
    like             = models.ManyToManyField(User,through='Userproductlike',related_name='products')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'products'

class Category(models.Model):
    name = models.CharField(max_length=16)
    
    class Meta:
        db_table = 'categories'

class Image(models.Model):
    url     = models.CharField(max_length=2048)
    product = models.ForeignKey('product', on_delete=models.CASCADE)

    class Meta:
        db_table = 'images'

class DescriptionImage(models.Model):
    url     = models.CharField(max_length=2048)
    product = models.ForeignKey('product', on_delete=models.CASCADE)

    class Meta:
        db_table = 'descriptionimages'

class UserProductLike(models.Model):
    user    = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        db_table = 'userproductlikes'
        unique_together = (("user","product"),)
