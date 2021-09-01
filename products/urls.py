from django.urls import path
from .views import MainPageView
urlpatterns = [
    path('/main', MainPageView.as_view())
]
