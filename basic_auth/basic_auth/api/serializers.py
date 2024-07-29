from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers




class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'email', 'first_name', 'last_name', 'is_active']



class RegisterViewSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True, required = True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)

    class Meta:
        model = get_user_model()
        fields = ['id', 'email', 'first_name', 'last_name', 'password']


    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            email = validated_data['email'],
            password= validated_data['password'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name']
        )
        return user
    


class LoginViewSerializer(serializers.Serializer):
    email = serializers.CharField(required = True)
    password = serializers.CharField(required = True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        user = authenticate(email=email, password=password)

        if user is None:
            raise serializers.ValidationError('Invalid Username or Password..')
        
        return data
