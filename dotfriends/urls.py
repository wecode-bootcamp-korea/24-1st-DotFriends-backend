from django.urls import path, include, re_path
from products.views import ListView

urlpatterns = [
    path('user', include('users.urls')),
    path('category', ListView.as_view()),
]

