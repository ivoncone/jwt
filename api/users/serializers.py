from rest_framework import serializers

from django.contrib.auth.models import User
from .models import User


class UserSerializer(serializers.ModelSerializer):
	model = User
	fields = '__all__'
	extra_kwargs = {
	'password': {'write_only': True},
	}