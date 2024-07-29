from django.shortcuts import render, get_object_or_404
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import *
from .models import *
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
    


class UserView(APIView):
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]
    def get(self, request, id=None):
        if id is None:
            querry = CustomUser.objects.all()
            serialized_querry = CustomUserSerializer(querry, many=True)
            return Response(serialized_querry.data, status=status.HTTP_200_OK)
        else:
    
            query = get_object_or_404(CustomUser, id=id)
            seralized_query = CustomUserSerializer(query, partial=True)
            return Response(seralized_query.data, status=status.HTTP_200_OK)
        

