from django.urls import path
from .views import CartListView

urlpatterns = [
    path('', CartListView.as_view()),
    path('/product/<int:product_id>', CartListView.as_view())
]
