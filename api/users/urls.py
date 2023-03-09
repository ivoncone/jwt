from django.urls import path

from users import views
from users.views import UserSignUpView

urlpatterns = [
	path('signup/', views.UserSignUpView.as_view())
]