from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer, PostSerializer
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import AuthenticationFailed
from .models import User, Post
from .secrete_token import SECRETE_KEY
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken



class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('User not found.')
        
        if not user.check_password(password):
            raise AuthenticationFailed('Invalid Username or Password.')

        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        refresh_token = str(refresh)

        return Response({
            'access': access_token,
            'refresh': refresh_token
        }, status=status.HTTP_200_OK)



class UserView(APIView):
    def get(self, request):
        token = request.headers.get('Authorization')
        if not token:
            raise AuthenticationFailed('Please log in.')

        if token.startswith('Bearer '):
            token = token.split(' ')[1]
        else:
            raise AuthenticationFailed('Invalid token format.')

        try:
            payload = AccessToken(token)
            user_id = payload['user_id']  # or 'id', depending on your token payload
            user = User.objects.get(id=user_id)
        except TokenError:
            raise AuthenticationFailed('Invalid token - Token error.')
        except InvalidToken:
            raise AuthenticationFailed('Invalid token - Invalid token.')
        except User.DoesNotExist:
            raise AuthenticationFailed('User not found.')

        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class LogoutView(APIView):
    def post(self, request):
        refresh_token = request.data.get('refresh')
        if refresh_token:
            try:
                token = RefreshToken(refresh_token)
                token.blacklist()
            except Exception:
                raise AuthenticationFailed('Invalid refresh token.')

        return Response({'message': 'Success..'}, status=status.HTTP_200_OK)
    


class PostView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        try:
            serializer = PostSerializer(data=request.data, context={'request':request})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except TokenError as e:
            return Response({'detail': str(e)}, status=status.HTTP_401_UNAUTHORIZED)

    
    def get(self, request, pk=None):
        id = pk
        if pk is not None:
            posted_data = get_object_or_404(Post, pk=id)
            serializer = PostSerializer(posted_data, partial=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:        
            all_data = Post.objects.all()
            serialized_data = PostSerializer(all_data, many=True)
            return Response(serialized_data.data, status=status.HTTP_200_OK)