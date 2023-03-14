from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.hashers import check_password

from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.permissions import AllowAny, IsAuthenticated

from rest_framework_simplejwt.tokens import AccessToken, RefreshToken

from .models import User 
from .serializers import UserSerializer

import datetime
from datetime import timedelta


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

class LoginView(APIView):
	permission_classes = [AllowAny]
	def post(self, request):
		email = request.data['email']
		password = request.data['password']
		user = User.objects.filter(email=email).first()

		if user is None:
			return Response({'status': 404,
				'message': 'User not found'})
		if not user.check_password(password):
			return Response({'status': 401, 'message': 'Incorrect password'})

		access = AccessToken.for_user(user)
		refresh = RefreshToken.for_user(user)

		response = Response()

		response.data = {
			'access': str(access),
			'refresh': str(refresh),
			'status': 200,
			'id': user.id,
		}

		return response



