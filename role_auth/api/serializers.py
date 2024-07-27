from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name', 'is_active')



class RegisterUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True,  required=True, min_length=8)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)

    class Meta:
        model = get_user_model()
        fields = ('id','email', 'password', 'first_name', 'last_name')

    
    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            first_name = validated_data.get('first_name', ''),
            last_name = validated_data.get('last_name', '')
        )

        return user


class LoginViewSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email']=user.email
        token['first_name']=user.first_name
        token['last_name']=user.last_name

        return token
    

class LogoutViewSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs

    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except Exception as e:
            self.fail('Invalid token.')
