from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import Token
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import CustomUser
from .serializers import *
import logging
# Create your views here.


logger = logging.getLogger(__name__)



class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        request_data = RegisterUserSerializer(data=request.data)
        
        if request_data.is_valid(raise_exception=True):
                try:
                    request_data.save()
                    return Response(request_data.data, status=status.HTTP_201_CREATED)
            
                except Exception as e:
                    logger.error('Exception occurred: %s', str(e))
                    return Response({'error': 'An unexpected error occurred.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(request_data.errors, status=status.HTTP_400_BAD_REQUEST)
        



class LoginView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer



class LogoutView(APIView):
    def post(self, request):
        serializer = LogoutViewSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message':'success'}, status=status.HTTP_204_NO_CONTENT)
    

class UserView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request, pk=None):
        user = request.user
        if pk is not None:
            try:
                user_data = CustomUser.objects.get(pk=pk)
                serialized_user = CustomUserSerializer(user_data, partial=True)
                return Response(serialized_user.data, status=status.HTTP_200_OK)
            except CustomUser.DoesNotExist:
                return Response({'error':f'user with id: {pk} does not match.'})
        else:
            serialized_user = CustomUserSerializer(user, partial=True)
            return Response(serialized_user.data, status=status.HTTP_200_OK)