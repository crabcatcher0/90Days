from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import Token
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import CustomUser
from .serializers import *
# Create your views here.


class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        request_data = RegisterUserSerializer(data=request.data)
        try:
            if request_data.is_valid(raise_exception=True):
                request_data.save()
                return Response(request_data.data, status=status.HTTP_201_CREATED)
            else:
                return Response(request_data.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error':str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

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