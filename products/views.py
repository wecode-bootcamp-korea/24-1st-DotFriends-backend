import json
import base64

from urllib.parse import unquote
from django.http  import JsonResponse
from django.views import View
from django.core.paginator import Paginator

from products.models import Product, Category

class PageView(View):
    def get(self, request):
        try:
            url = request.path_info

            results = []
            products = []

            description_style   = request.GET.get('st')
            current_page        = request.GET.get('page')
            page_size           = int(request.GET.get('size'))
            encoded             = request.GET.get('encoded')

            decoded       = base64.b64decode(encoded).decode('utf-8')
            category_name = unquote(decoded)
            category = Category.objects.get(name=category_name)

            if description_style == 'recent':
                products = Product.objects.filter(category_id=category.id).order_by('-updated_at')

            if description_style == 'lowPrice':
                products = Product.objects.filter(category_id=category.id).order_by('price')

            if description_style == 'highPrice':
                products = Product.objects.filter(category_id=category.id).order_by('-price')

            total_page = round(len(products)/page_size)

            for product in products:
                price = int(product.price)
                results.append(
                    {
                        'id'               : product.id,
                        'name'             : product.name,
                        'price'            : price,
                        'image'            : product.image_set.values_list('url')[0][0]
                    }
                )
            pagination = Paginator(results, page_size)
            paged_list = pagination.page(current_page).object_list
            total_products = len(results)

            return JsonResponse({'MESSAGE':'SUCCESS', 'results':paged_list, 'totalPage':total_page, 'totalProducts': total_products}, status=200)

        except KeyError:
            return JsonResponse({'MESSAGE':'KEY_ERROR'}, status=400)

