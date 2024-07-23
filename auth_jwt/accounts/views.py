from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework.exceptions import AuthenticationFailed
from .models import User
import jwt, datetime
from .secrete_token import SECRETE_KEY
from jwt.exceptions import DecodeError, ExpiredSignatureError, InvalidTokenError


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
        
        expiration_time = datetime.datetime.now(datetime.UTC) + datetime.timedelta(minutes=60)

        payload = {
            'id':user.id,
            'exp':expiration_time,
            'iat':datetime.datetime.now(datetime.UTC)
        }

        token = jwt.encode(payload, SECRETE_KEY, algorithm='HS256')

        # response = Response()
        # response.set_cookie(key='jwt', value=token, httponly=True)
        # response.data = {
        #     'message':'success'
        # }
        
        return Response(token, status=status.HTTP_200_OK)
    

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
            payload = jwt.decode(token, SECRETE_KEY, algorithms=['HS256'])

        except ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated - Token has expired.')
        
        except DecodeError:
            raise AuthenticationFailed('Invalid token - Decode error.')
        
        except InvalidTokenError:
            raise AuthenticationFailed('Invalid token - Invalid token error.')
        

        user = User.objects.filter(id=payload['id']).first()
        if user is None:
            raise AuthenticationFailed('User not found.')

        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message':'success'
        }
        return response