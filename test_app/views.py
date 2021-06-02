from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Test, Question, Answer, UserAnswer


def index_view(request):
    test = Test.objects.get(pk=1)
    return render(request, 'add_test.html', context={'test': test})


class HomeView(ListView):
    template_name = 'add_test.html'
    model = Test



