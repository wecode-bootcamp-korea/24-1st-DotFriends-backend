import json

from django.http.response import JsonResponse
from django.views         import View

from .models          import Cart
from products.models  import Product
from users.decorators import login_decorator

class CartView(View):
    @login_decorator
    def post(self, request):
        try:
            data       = json.loads(request.body)
            user       = request.user
            product_id = data['product_id']
            quantity   = data['quantity']

            if not Product.objects.filter(id=product_id).exists():
                return JsonResponse({'MESSAGE':'DOES_NOT_EXIST_PRODUCT'}, status = 404)

            Cart.objects.create(
                user       = user,
                product_id = product_id,
                quantity   = quantity
            )
            return JsonResponse({'MESSAGE':'CREATE'}, status = 201)

        except KeyError:
            return JsonResponse({'MESSAGE':'KEY_ERROR'}, status = 400)
        except ValueError:
            return JsonResponse({'MESSAGE':'VALUE_ERROR'}, status = 400)

    @login_decorator
    def get(self, request):

        user = request.user
        carts = Cart.objects.filter(user_id=user).select_related('product')
        
        result = [{
            'name' : cart.product.name,
            'price': int(cart.product.price),
            'image': [image.url for image in cart.product.image_set.all()],
            'quantity' : cart.quantity
        }for cart in carts]

        return JsonResponse({'result':result}, status = 201)