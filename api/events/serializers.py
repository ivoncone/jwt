from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from events.models import Events



class EventSerializer(serializers.ModelSerializer):

	class Meta:
		model = Events
		fiels = ['__all__']

