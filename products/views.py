import re
import json

from django.http      import JsonResponse
from django.views     import View
from django.db.models import Q

from .models         import Product

class ProductOptionView(View):
    def get(self, request):
        option = request.GET.get('option', None)
        offset = request.GET.get('offset', 0)
        limit  = request.GET.get('limit', 12)
        order  = request.GET.get('order', None)
        order_option = {'random':"?", 'asc':"id", 'desc':"-id"}  

        if order not in order_option:
            order = 'asc'
        order = order_option[order]

        if option != 'new' and option != 'sale':
            return JsonResponse({'MESSAGE': 'WRONG_ACCESS'}, status=400)
        
        if not (re.match('^[0-9][0-9]*$', str(offset)) and re.match('^[0-9][0-9]*$', str(limit))):
            offset, limit = 0, 12
        offset, limit = int(offset), int(limit)
       
        q = Q()
        if option == 'new':
            q = Q(is_new=True)
           
        if option == 'sale':
            q = Q(~Q(discount_percent=0))    
        
        count = Product.objects.filter(q).order_by(order).count()
        if count < (limit + offset): offset, limit = 0, 12
        products = Product.objects.filter(q).order_by(order)[offset:limit+1]
        
        results = [{
            'id'    : product.id,
            'name'  : product.name,
            'price' : int(product.price)
        }for product in products]

        return JsonResponse({'results': results}, status=200)  

