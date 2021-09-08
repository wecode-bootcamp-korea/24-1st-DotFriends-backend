from django.urls import path
from .views import ProductsView, ProductDetailView

urlpatterns = [
    path('', ProductsView.as_view()),
    path('/<int:product_id>', ProductDetailView.as_view())
]