from django.db import models

from users.models    import User
from products.models import Product

class Comment(models.Model):
    user       = models.ForeignKey(User, on_delete=models.CASCADE)
    product    = models.ForeignKey(Product, on_delete=models.CASCADE)
    rate       = models.DecimalField(max_digits=5, decimal_places=3)
    text       = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'comments'

class CommentImage(models.Model):
    url     = models.CharField(max_length=2048)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)

    class Meta:
        db_table = 'commentimages'


