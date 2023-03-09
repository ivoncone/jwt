from django.shortcuts import render
from django.contrib import messages

from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import User 
from .serializers import UserSerializer

# New user register
class UserSignUpView(APIView):
	permission_classes = [AllowAny]
	def post(self, request):
		serializer = UserSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response({'status': 201,
			'message':'user has been created successfully'})
		else:
			return Response({'status':403, 'message': 'email already exists'})

