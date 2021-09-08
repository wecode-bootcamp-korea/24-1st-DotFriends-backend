import json
import re
import base64

from urllib.parse import unquote
from django.http  import JsonResponse
from django.db.models import Q, Count, Avg
from django.http      import JsonResponse
from django.views     import View

from .models          import Product, Category, UserProductLike
from comments.models  import Comment
from .decorator       import input_validator, visitor_validator

class ListView(View):
    def get(self, request):
        try:
            results = []
            products = []

            ordering            = request.GET.get('ordering')

            offset              = int(request.GET.get('offset'))
            limit               = int(request.GET.get('limit'))

            encoded             = request.GET.get('encoded')
            decoded             = base64.b64decode(encoded).decode('utf-8')
            request_category_id = unquote(decoded)

            if not (ordering=='popular' or ordering=='-updated_at' or ordering =='price' or ordering =='-price'):
                return JsonResponse({'MESSAGE':'INVALID ORDERING'}, status=400)
            products = Product.objects.filter(category_id=request_category_id).annotate(popular=Count("userproductlike")).order_by(ordering)[offset:offset+limit]

            total_page = round(len(products)/limit)

            for product in products:
                price = int(product.price)
                results.append(
                    {
                        'id'               : product.id,
                        'name'             : product.name,
                        'price'            : price,
                        'image'            : product.image_set.values_list('url')[0][0],
                        'updated_at'       : product.updated_at,
                        'popular'          : product.popular
                    }
                )

            total_products = len(results)
            return JsonResponse({'MESSAGE':'SUCCESS', 'results':results, 'totalPage':total_page, 'totalProducts': total_products}, status=200)

        except KeyError:
            return JsonResponse({'MESSAGE':'KEY_ERROR'}, status=400)

class ProductsView(View):
    @input_validator
    def get(self, request):
        option = request.GET.get('option', None)
        offset = int(request.GET.get('offset', 0))
        limit  = int(request.GET.get('limit', 10))
        order  = request.GET.get('order', 'id')
        search = request.GET.get('search', None)
    
        q = Q()
        if option == 'new':
            q = Q(is_new=True)
        
        if option == 'sale':
            q = Q(~Q(discount_percent=0))

        if search:
            q &= Q(name__icontains = search)

        products = Product.objects.filter(q).prefetch_related('image_set').order_by(order)[offset:offset+limit]
        total_count = Product.objects.filter(q).count()
        
        results = [{
            'id'    : product.id,
            'name'  : product.name,
            'price' : int(product.price),
            'images':[image.url for image in product.image_set.all()]
        }for product in products]

        return JsonResponse({'results': results, 'count': total_count}, status=200)  
        
class ProductDetailView(View):
    @visitor_validator
    def get(self, request, product_id):
        
        if not (Product.objects.filter(id=product_id).exists()):
            return JsonResponse({'MESSAGE': 'NOT_FOUND'}, status=404)
        
        product  = Product.objects.annotate(avg_rate=Avg('comment__rate'),likes=Count("userproductlike", distinct=True)\
            ,comment_count=Count('comment',distinct=True)).get(id=product_id)
        comments = Comment.objects.filter(product_id=product_id).select_related('user').prefetch_related('commentimage_set')
        likes = None
        if request.user:
            if UserProductLike.objects.filter(user_id=request.user.id,product_id=product_id).exists():
                likes = 'Yes'
                
        
        results = {
            'id'           :product.id,
            'name'         :product.name,
            'price'        :int(product.price),
            'likes'        : product.likes,
            'is_new'       : product.is_new,
            'isLiked'      : True if likes else False,
            'comment_avg_rate' : round(product.avg_rate,1),
            'comment_count':product.comment_count,
            'images'       :[image.url for image in product.image_set.all()],
            'reviews' :[{
                "user_name" :comment.user.name,    
                "rate"      : int(comment.rate),
                "text"      : comment.text,
                "created_at": comment.created_at.date(),
                "images"    : [image.url for image in comment.commentimage_set.all()]
            }for comment in comments]}
                
        return JsonResponse({'results': results}, status=200)