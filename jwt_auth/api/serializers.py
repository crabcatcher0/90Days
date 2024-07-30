from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import *


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'first_name', 'last_name', 'is_active', 'password')



class RegisterViewSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    first_name = serializers.CharField(required = True)
    last_name = serializers.CharField(required = True)

    class Meta:
        model = get_user_model()
        fields = ('email', 'password', 'first_name', 'last_name')

    
    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            email=validated_data['email'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name']

        )
        user.set_password(validated_data['password'])
        user.save()
        return user



class LoginViewSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name
        return token
