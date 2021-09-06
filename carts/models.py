from django.db import models

from users.models import User
from products.models import Product

class Cart(models.Model):
    user          = models.ForeignKey(User, on_delete=models.CASCADE, related_name='carts')
    product       = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='carts')
    quantity      = models.IntegerField(default=0)
    created_at    = models.DateTimeField(auto_now_add=True)
    updated_at    = models.DateTimeField(auto_now=True)

class Meta:
    db_table = 'carts'