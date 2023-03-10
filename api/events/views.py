from django.shortcuts import render

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

from events.models import Events
from events.serializers import EventSerializer

# Show the list of all events in website
class EventsView(APIView):
	def get(self, request):
		events = Events.objects.all()
		serializer = EventSerializer(events, many=True)
		return Response({'status': 200,
			'message': serializer.data})

	def post(self, request):
		data = request.data
		serializer = EventSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return Response({'status': 201,
				'message': 'your event has been post',
				'data': serializer.data})
		return Response({'status': 400, 'message': 'algun dato falta'})

