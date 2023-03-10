from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from events.models import Events



class EventSerializer(serializers.ModelSerializer):

	class Meta:
		model = Events
		fiels = ['event_name', 'event_description', 'placee','contact', 'reservation', 'date']

