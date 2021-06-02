from django.urls import path
from .views import index_view, HomeView, RegistrationView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('registration', RegistrationView.as_view(), name='registration'),
    path('add_test', index_view, name='add_test')
]