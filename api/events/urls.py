from django.urls import path

from events import views
from events.views import EventsView

urlpatterns = [
	path('events/', views.EventsView.as_view())
]