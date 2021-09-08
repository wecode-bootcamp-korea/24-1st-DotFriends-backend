from django.urls import path, include, re_path

urlpatterns = [
    path('product', include('products.urls')),
    path('user', include('users.urls'))
]

