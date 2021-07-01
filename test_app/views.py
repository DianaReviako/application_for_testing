from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import DetailView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from testing.settings import LOGOUT_REDIRECT_URL
from .forms import RegisterUser, AddTestNameForm, AddQuestionForTestForm,  AddAnswerForQuestionForm
from .models import Test, Answer, UserAnswer, Question


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


class UserCreatedTestView(TemplateView):
    """The page that displays the user-generated test"""
    template_name = 'test.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        test = Test.objects.latest('id')
        context['test'] = test
        context['questions'] = test.question_set.all()
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

    def get_success_url(self):
        return reverse_lazy('login')


class LoginUserView(LoginView):
    """Allows the user to log in. If successful, redirects to a page with a
       welcome and links to add a new test or the ability to go to a page with all available tests."""
    form_class = AuthenticationForm
    template_name = 'login.html'

    def get_success_url(self):
        return reverse_lazy('success_login')


class LogoutUserView(LogoutView):
    redirect_field_name = LOGOUT_REDIRECT_URL
    template_name = 'home.html'


class AddTestView(CreateView):
    """Provides a form for the ability to add a new test(title)"""
    template_name = 'add_test.html'
    form_class = AddTestNameForm

    def get_success_url(self):
        return reverse_lazy('test')


class AddQuestionView(CreateView):
    """Allows the user to add a question to a test they have created"""
    template_name = 'add_question.html'
    form_class = AddQuestionForTestForm

    def get_success_url(self):
        return reverse_lazy('test')


class AddAnswerView(CreateView):
    template_name = 'add_answer.html'
    form_class = AddAnswerForQuestionForm

    def get_success_url(self):
        return reverse_lazy('test')


class TestView(DetailView):
    """Displaying the test on the page. If the user has already passed the test,
    the user will be notified about this and the test will not be displayed."""
    model = Test
    template_name = 'take_test.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        test_id = self.kwargs['pk']
        user_id = self.request.user.id
        test_already_passed = UserAnswer.objects.filter(user=user_id, test=test_id)
        test = Test.objects.get(id=test_id)
        context['test'] = test
        context['test_already_passed'] = test_already_passed
        return context


class SaveUserResultView(CreateView):
    """Saving the user's answers."""
    model = UserAnswer

    def dispatch(self, request, *args, **kwargs):
        if request.method == 'POST':
            username = request.user
            test_id = int(request.POST['test_id'])
            for key in request.POST.keys():
                if key not in ('csrfmiddlewaretoken', 'test_id', 'answer_id'):
                    question_id, answer_id = key.split('#')
                    user_result = UserAnswer.objects.create(
                        user=username,
                        test=Test(id=test_id),
                        question=Question(id=int(question_id)),
                        answer=Answer(id=int(answer_id))
                        )
        try:
            return redirect('result', pk=user_result.id)
        except UnboundLocalError:
            return render(request, 'take_test.html', context={'no_answer': "You haven't answered any question", 'UnboundLocalError': UnboundLocalError})


class SeeTheResultView(DetailView):
    """Demonstration to the user his mark for the test.
    A point is counted if all correct answer options are selected for the question."""
    template_name = 'view_result.html'
    model = UserAnswer
    context_object_name = 'user_result'

    def get_context_data(self, **kwargs):
        context = super(SeeTheResultView, self).get_context_data(**kwargs)
        test_id = self.object.test_id
        user_id = self.request.user.id
        user_results_per_test = UserAnswer.objects.filter(user=user_id, test=test_id)
        test_score = 0
        question_id = []
        for user_result in user_results_per_test:
            question_id.append(user_result.question.id)
            number_of_duplicate_id = question_id.count(user_result.question.id)
            correct_answers_to_the_question = Answer.objects.filter(question=user_result.question.id, correct=True)

            user_answer_to_this_question = [
                result.answer.correct for result in user_results_per_test.filter(question=user_result.question.id)
            ]
            if len(correct_answers_to_the_question) == len(user_answer_to_this_question) and\
                    all(user_answer_to_this_question) and number_of_duplicate_id < 2:
                test_score += 1
        context['test_score'] = test_score
        return context




