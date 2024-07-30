from django.shortcuts import render, get_list_or_404
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import *


class Homeview(APIView):
    def get(self, request):
        return Response({'message:':'Hi, Welcome to Jwt Auth...'})
    
class UserView(APIView):
    def get(self, request):
        query = CustomUser.objects.all()
        serialized_data = CustomUserSerializer(query, many=True)
        return Response(serialized_data.data, status=status.HTTP_200_OK)
    

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serialized_query = CustomUserSerializer(data=request.data)
        if serialized_query.is_valid():
            try:
                serialized_query.save()
                return Response({'message:':'success'}, status=status.HTTP_200_OK)
            except:
                return Response(serialized_query.errors, status=status.HTTP_400_BAD_REQUEST)
            


class LoginView(TokenObtainPairView):
    serializer_class = LoginViewSerializer