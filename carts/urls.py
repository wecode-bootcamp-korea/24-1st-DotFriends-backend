from django.urls import path
from .views import CartView

urlpatterns = [
    path('', CartView.as_view()),
    path('/<int:product_id>', CartListView.as_view())
]
