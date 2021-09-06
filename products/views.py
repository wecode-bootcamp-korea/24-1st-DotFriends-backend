from django.http      import JsonResponse
from django.views     import View
from django.db.models import Q

from .models          import Product
from .decorator       import input_validator

class ProductsView(View):
    @input_validator
    def get(self, request):
        option = request.GET.get('option', None)
        offset = int(request.GET.get('offset', 0))
        limit  = int(request.GET.get('limit', 0))
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
