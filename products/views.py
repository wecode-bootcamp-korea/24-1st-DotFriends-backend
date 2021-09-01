import json

from django.http      import JsonResponse
from django.views     import View
from django.db.models import Q

from .models         import Product

class MainPageView(View):
    def get(self, request):
        option = request.GET.get('option',None)

        if option != 'new' and option != 'sale':
            return JsonResponse({'MESSAGE': 'WRONG_ACCESS'}, status=400)

        q = Q()
        if option == 'new':
            q = Q(is_new=True)
           
        if option == 'sale':
            q = Q(~Q(discount_percent=0))    

        products = Product.objects.filter(q).order_by("?")[:12]
        
        results = [{
            'id'    : product.id,
            'name'  : product.name,
            'price' : int(product.price)
        }for product in products]

        return JsonResponse({'results': results}, status=200)  
