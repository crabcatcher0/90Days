from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import *
# Create your views here.


class HomeView(APIView):

    def get(self, request):
        return Response({'message: ':'Hello, Welcome.'}, status=status.HTTP_200_OK)
    

class RegisterView(APIView):
    def post(self, request):
        serialized_data = RegisterViewSerializer(data=request.data)
        if serialized_data.is_valid():
            try:
                serialized_data.save()
                return Response(serialized_data.data, status=status.HTTP_201_CREATED)
            
            except Exception:
                return Response({'error': 'An unexpected error occurred.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        else:
            return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)
        


class LoginView(APIView):    
    def post(self, request):
        serialzed_data = LoginViewSerializer(data=request.data)
        if serialzed_data.is_valid():
            return Response({'message:':'logged in'}, status=status.HTTP_200_OK)
    
        return Response(serialzed_data.data, status=status.HTTP_400_BAD_REQUEST)
    
            