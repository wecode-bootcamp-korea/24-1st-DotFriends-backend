from django.views import View
from django.http import JsonResponse

from .models import Product

class ProductSearchView(View):
    def get(self, request):

        page          = int(request.GET.get('page', 1))
        limit         = int(request.GET.get('limit', 5))
        offset        = (page-1) * limit
        search        = request.GET.get('search', None)
        products_all  = Product.objects.prefetch_related('image_set').filter(name__icontains = search)
        count         = products_all.count()
        products      = products_all[offset:offset + limit]
        
        results = [{
            'id'    : product.id,
            'name'  : product.name,
            'price' : int(product.price),
            'images': product.image_set.all()[0].url
            }for product in products]

        return JsonResponse({'results': results, 'count': count}, status=200)