from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from .models import Test
from .forms import RegisterUser


class HomeView(TemplateView):
    template_name = 'home.html'


class RegistrationView(CreateView):
    """User registration"""
    template_name = 'registration.html'
    form_class = RegisterUser
    success_url = 'add_test'


def index_view(request):
    """Temporary stub function"""
    test = Test.objects.get(pk=1)
    return render(request, 'add_test.html', context={'test': test})





