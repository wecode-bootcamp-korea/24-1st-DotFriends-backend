from django.urls import path
from .views import ProductOptionView
urlpatterns = [
    path('', ProductOptionView.as_view())
]
