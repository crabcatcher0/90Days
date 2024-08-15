from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .serializers import *
# Create your views here.


class HomeView(APIView):
    def get(self, request):
        return Response({'message':'Hello, Welcome.'}, status=status.HTTP_200_OK)
    

class RegisterView(APIView):
    def post(self, request):
        data = RegistrationSerializer(data = request.data)
        if data.is_valid():
            data.save()
            return Response(data.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
        

class LoginView(APIView):
    def post(self, request):
        data = LoginSerializer(data = request.data)

        if data.is_valid():
            username = data.validated_data['username']
            password = data.validated_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return Response({'message':'success...'}, status=status.HTTP_200_OK)
            else:
                return Response({'message':'Invalid Creds..'}, status=status.HTTP_400_BAD_REQUEST)
            
        return Response(data.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
