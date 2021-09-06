import re
import json

from django.http      import JsonResponse
from django.views     import View
from django.db.models import Q, Count

from .models          import Product
from comments.models  import Comment
from .decorator       import input_validator

class ProductsView(View):
    @input_validator
    def get(self, request):
        option = request.GET.get('option', None)
        offset = int(request.GET.get('offset', 0))
        limit  = int(request.GET.get('limit', 10))
        order  = request.GET.get('order', 'id')
    
        q = Q()
        if option == 'new':
            q = Q(is_new=True)
        
        if option == 'sale':
            q = Q(~Q(discount_percent=0))
        
        products = Product.objects.filter(q).prefetch_related('image_set').order_by(order)[offset:offset+limit]
        
        results = [{
            'id'    : product.id,
            'name'  : product.name,
            'price' : int(product.price),
            'images':[image.url for image in product.image_set.all()]
        }for product in products]

        return JsonResponse({'results': results}, status=200)  

class ProductDetailView(View):
    def get(self, request, product_id):
        
        if not (Product.objects.filter(id=product_id).exists()):
            return JsonResponse({'MESSAGE': 'NOT_FOUND'}, status=404)

        product  = Product.objects.annotate(likes=Count("userproductlike")).get(id=product_id)
        comments = Comment.objects.filter(product_id=product_id).select_related('user').prefetch_related('commentimage_set')
        
        results = {
            'id'      :product.id,
            'name'    :product.name,
            'price'   :int(product.price),
            'like'    : product.likes,
            'images'  :[image.url for image in product.image_set.all()],
            'reviews' :[{
                "user_name" :comment.user.name,    
                "rate"      : int(comment.rate),
                "text"      : comment.text,
                "created_at": comment.created_at.date(),
                "images"    : [image.url for image in comment.commentimage_set.all()]
            }for comment in comments]}
                
        return JsonResponse({'results': results}, status=200)