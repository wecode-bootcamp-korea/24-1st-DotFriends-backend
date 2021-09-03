import json
import re
import base64

from urllib.parse import unquote
from django.http  import JsonResponse
from django.http.response import HttpResponse
from django.views import View
from django.core.paginator import Paginator
from django.db.models import Q, Count

from products.models import Product, Category

from .models          import Product
from .decorator       import input_validator  

class ListView(View):
    def get(self, request):
        try:
            url = request.path_info

            results = []
            products = []

            ordering            = request.GET.get('ordering')

            page                = int(request.GET.get('page'))
            limit               = int(request.GET.get('limit'))

            encoded             = request.GET.get('encoded')
            decoded             = base64.b64decode(encoded).decode('utf-8')
            category_name       = unquote(decoded)
            category            = Category.objects.get(name=category_name)

            if not (ordering=='popular' or ordering=='-updated_at' or ordering =='price' or ordering =='-price'):
                return JsonResponse({'MESSAGE':'정렬기준 제대로 부탁합니당'}, status=400)
            total_count = Product.objects.filter().count()
            products = Product.objects.filter(category_id=category.id).annotate(popular=Count("userproductlike")).order_by(ordering)[offset:limit]

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

            offset         = (page-1)*limit
            total_products = len(results)
            result_list    = results[offset:offset+limit]

            return JsonResponse({'MESSAGE':'SUCCESS', 'results':result_list, 'totalPage':total_page, 'totalProducts': total_products}, status=200)

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
