from rest_framework import serializers
from django.contrib.auth.models import User


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password']
        extra_kwargs = {
            'password':{'write_only': True}
        }

    def create(self, validated_data):
            user = User(
                username = validated_data['username'],
                email = validated_data['email'],
                first_name = validated_data['first_name'],
                last_name = validated_data['last_name']
            )

            user.set_password(validated_data['password'])
            user.save()
            return user



class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only = True)
    class Meta:
        model = User
        fields = ['username', 'password']

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            raise serializers.ValidationError("Both username and password are required.")
        return data
