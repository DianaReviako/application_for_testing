from django.urls import path
from .views import index_view, HomeView
urlpatterns = [
    path('', HomeView.as_view(), name='index'),
]