from django.urls import path, include, re_path

urlpatterns = [
    path('product', include('products.urls')),
    path('user', include('users.urls')),
    path('cart', include('carts.urls'))
]
