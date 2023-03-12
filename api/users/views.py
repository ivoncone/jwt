from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.hashers import check_password

from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.permissions import AllowAny, IsAuthenticated

from rest_framework_simplejwt.tokens import RefreshToken

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

		payload = {
			'id': user.id,
			'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
			'iat': datetime.datetime.utcnow()
		}

		refresh = RefreshToken.for_user(user)

		response = Response()

		response.data = {
			'access': str(refresh.access_token),
			'refresh': str(refresh),
			'status': 200,
			'id': user.id,

		}

		return response

class UserView(APIView):
	permission_classes = [IsAuthenticated]

	def get(self, request):
		user = User.objects.get(email=request.user)
		if User.objects.filter(user=user).exists():
			user = User.objects.filter(user=user).first()
			serializer = UserSerializer(user)
			return Response({'status':200, 'data': serializer.data})
		return Response({'status': 404, 'message': 'este usuario no ha sido creado'})

