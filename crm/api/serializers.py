from rest_framework import serializers
from django.contrib.auth.models import User


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password']


class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only = True)
    class Meta:
        model = User
        fields = ['username', 'password']

    def validate(self, data):
        username = data.get['username']
        password = data.get['password']

        if username and password is None:
            raise serializers.ValidationError("Both are required.")
        
        return data
