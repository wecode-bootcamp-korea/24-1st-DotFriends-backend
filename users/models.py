from django.db import models

class User(models.Model):
    name         = models.CharField(max_length=32)
    email        = models.CharField(max_length=64)
    password     = models.CharField(max_length=512)
    phone_number = models.CharField(max_length=16)
    address      = models.CharField(max_length=128)

    class Meta:
        db_table = 'users'