from django.urls import path, include, re_path
from products.views import PageView

urlpatterns = [
    path('user', include('users.urls')),
    re_path(r'^category/[a-zA-Z0-9]+$', PageView.as_view())
]
