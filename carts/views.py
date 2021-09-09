import json

from django.http.response import JsonResponse
from django.views         import View
from django.db.models import Q

from .models          import Cart
from products.models  import Product
from users.models     import User
from users.decorators import login_decorator

class CartListView(View):
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

    @login_decorator
    def delete(self, request):
        try:
            parts = urlparse(request.get_full_path())
            product_ids = parse_qs(parts.query)['product_id']

            Cart.objects.filter(user_id=request.user.id, product_id__in = product_ids).delete()

            return JsonResponse({'MESSAGE':'NO_CONTENT'}, status=204)

        except KeyError:
            return JsonResponse({'MESSAGE':'KEY_ERROR'}, status=400)

    @login_decorator
    def patch(self, request):
        try:
            data = json.loads(request.body)

            cart = Cart.objects.get(user_id=request.user.id, product_id=data['productId'])

            cart.quantity = data['quantity']
            cart.save()

            return JsonResponse({'MESSAGE':'NO_CONTENT'}, status=204)

        except KeyError:
            return JsonResponse({'MESSAGE':'KEY_ERROR'}, status=400)
        
        except Cart.DoesNotExist:
            return JsonResponse({'MESSAGE':'INVALID_CART_ITEM'}, status=400)

