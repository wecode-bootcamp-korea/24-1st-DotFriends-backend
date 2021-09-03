import json
import base64

from urllib.parse import unquote
from django.http  import JsonResponse
from django.views import View
from django.core.paginator import Paginator
from django.db.models import Count

from products.models import Product, Category

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
            else :
                products = Product.objects.filter(category_id=category.id).annotate(popular=Count("userproductlike")).order_by(ordering)

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
