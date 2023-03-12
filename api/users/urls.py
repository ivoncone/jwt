from django.urls import path

from users import views
from users.views import UserSignUpView, LoginView

urlpatterns = [
	path('signup/', views.UserSignUpView.as_view()),
	path('login/', views.LoginView.as_view()),
	
]