from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Test


class RegisterUser(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)


class AddTestForm(forms.ModelForm):
    """The form with which the user can create his own test"""
    class Meta:
        model = Test
        fields = ('title', )
