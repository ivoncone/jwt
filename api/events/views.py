from django.shortcuts import render

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

from events.models import Events
from events.serializers import EventSerializer

# Vista de todos los eventos en el sitio web
class EventsView(APIView):
	def get(self, request):
		events = Events.objects.all()
		serializer = EventsSerializer(events, many=True)
		return Response({'status': 200,
			'message': serializer.data})
