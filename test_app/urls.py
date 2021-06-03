from django.urls import path
from .views import HomeView, RegistrationView, LoginUserView, AddTestView, SuccessLoginView, UserCreateTestView, \
    AllAvailableTest

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('registration', RegistrationView.as_view(), name='registration'),
    path('login', LoginUserView.as_view(), name='login'),
    path('success_login', SuccessLoginView.as_view(), name='success_login'),
    path('add_test', AddTestView.as_view(), name='add_test'),
    path('test', UserCreateTestView.as_view(), name='test'),
    path('all_test', AllAvailableTest.as_view(), name='all_test')
]