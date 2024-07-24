from rest_framework import serializers
from .models import User, Post
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'full_name', 'email', 'password']
        extra_kwargs = {
            'password':{'write_only':True}
        }
    
    def validate_password(self, value):
        try:
            validate_password(value)
        except ValidationError as e:
            raise serializers.ValidationError(e.messages)
        return value


    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)

        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
    

class PostSerializer(serializers.ModelSerializer):
    full_name =  serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'user', 'full_name', 'title', 'content', 'created_at']
        read_only_fields = ['user']
    
    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        return super().create(validated_data)
    
    def get_full_name(self, obj):
        return obj.user.full_name
