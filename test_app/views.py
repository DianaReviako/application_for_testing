from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import RegisterUser, AddTestForm
from .models import Test


class HomeView(TemplateView):
    """Displaying the home page. If the user is not logged in, he will be taken to a page where he
       will be asked to register or log in. If logged in. then the user will be redirected to a page
       where he can add a task or go to existing tests"""
    template_name = 'home.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('success_login')
        else:
            return render(request, 'home.html')


class SuccessLoginView(TemplateView):
    """A page with a welcome and links to add a new test or the ability
       to go to a page with all available tests."""
    template_name = 'success_log.html'


class UserCreateTestView(TemplateView):
    """The page that displays the user-generated test"""
    template_name = 'test.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['test'] = Test.objects.latest('id')
        return context


class AllAvailableTest(TemplateView):
    """A view that shows the user all available tests"""
    template_name = 'all_test.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tests'] = Test.objects.all()
        return context


class RegistrationView(CreateView):
    """This class allows you to register a new user. If successful,
        redirects the user to the page where he can log in."""
    template_name = 'registration.html'
    form_class = RegisterUser
    reverse_lazy = 'login'


class LoginUserView(LoginView):
    """Allows the user to log in. If successful, redirects to a page with a
       welcome and links to add a new test or the ability to go to a page with all available tests."""
    form_class = AuthenticationForm
    template_name = 'login.html'

    def get_success_url(self):
        return reverse_lazy('success_login')


class AddTestView(CreateView):
    """Provides a form for the ability to add a new test"""
    template_name = 'add_test.html'
    form_class = AddTestForm

    def get_success_url(self):
        return reverse_lazy('test')


