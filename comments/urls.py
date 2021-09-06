from django.urls import path
from .views import CommentsView
urlpatterns = [
    path('/<int:product_id>', CommentsView.as_view()),
]
