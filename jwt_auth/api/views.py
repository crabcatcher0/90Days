from django.shortcuts import render, get_list_or_404
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *


class Homeview(APIView):
    def get(self, request):
        return Response({'message:':'Hi, Welcome to Jwt Auth...'})
    

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
            
    