from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Test, Question, Answer


class RegisterUser(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)


class AddTestNameForm(forms.ModelForm):
    """The form with which the user can create his own test(title)"""
    class Meta:
        model = Test
        fields = ('title', )


class AddQuestionForTestForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('test', 'type', 'text')


class AddAnswerForQuestionForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ('question', 'text', 'correct')


