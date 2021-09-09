from django.urls import path, include, re_path
#from products.views import ListView

urlpatterns = [
    #path('category', ListView.as_view()),
    path('product', include('products.urls')),
    path('user', include('users.urls'))
]

