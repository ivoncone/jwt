from django.urls import path

from users import views
from users.views import UserSignUpView, LoginView, UserView

urlpatterns = [
	path('signup/', views.UserSignUpView.as_view()),
	path('login/', views.LoginView.as_view()),
	path('user/', views.UserView.as_view())
]