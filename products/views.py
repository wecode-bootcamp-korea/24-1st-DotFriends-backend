import json
import re
import base64

from urllib.parse import unquote
from django.http  import JsonResponse
from django.http.response import HttpResponse
from django.core.paginator import Paginator
from django.db.models import Q, Count
from django.http      import JsonResponse
from django.views     import View

from products.models import Product, Category
from .decorator       import input_validator

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
        limit  = int(request.GET.get('limit', 0))
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
