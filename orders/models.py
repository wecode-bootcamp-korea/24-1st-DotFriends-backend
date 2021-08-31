from django.db import models

from users.models    import User
from products.models import Product

class Order(models.Model):
    user     = models.ForeignKey(User, on_delete=models.CASCADE)
    status   = models.ForeignKey('OrderStatus', on_delete=models.SET_NULL, null=True)
    datetime = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'orders'

class OrderStatus(models.Model):
    description = models.CharField(max_length=32)

    class Meta:
        db_table = 'orderstauts'

class OrderItemStatus(models.Model):
    description = models.CharField(max_length=32)

    class Meta:
        db_table = 'orderitemstatus'

class OrderItem(models.Model):
    order    = models.ForeignKey(Order, on_delete=models.CASCADE)
    product  = models.ForeignKey(Product, on_delete=models.CASCADE)
    status   = models.ForeignKey(OrderItemStatus, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price    = models.IntegerField()

    class Meta:
        db_table = 'orderitems'




