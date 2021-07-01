from django.urls import path
from .views import HomeView, RegistrationView, LoginUserView, AddTestView, SuccessLoginView, UserCreatedTestView, \
    AllAvailableTest, LogoutUserView, AddQuestionView, AddAnswerView, TestView, SaveUserResultView, SeeTheResultView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('registration', RegistrationView.as_view(), name='registration'),
    path('login', LoginUserView.as_view(), name='login'),
    path('success_login', SuccessLoginView.as_view(), name='success_login'),
    path('logout', LogoutUserView.as_view(), name='logout'),
    path('add_test', AddTestView.as_view(), name='add_test'),
    path('test', UserCreatedTestView.as_view(), name='test'),
    path('all_test', AllAvailableTest.as_view(), name='all_test'),
    path('add_question', AddQuestionView.as_view(), name='add_question'),
    path('add_answers', AddAnswerView.as_view(), name='add_answer'),
    path('take_test/<int:pk>', TestView.as_view(), name='take_test'),
    path('save_result/', SaveUserResultView.as_view(), name='save_result'),
    path('result/<int:pk>', SeeTheResultView.as_view(), name='result'),
]