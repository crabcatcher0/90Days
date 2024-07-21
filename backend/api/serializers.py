from rest_framework import serializers
from .models import *


class OfficialSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfficialName
        fields = ['id', 'first_name', 'last_name', 'position', 'added_at']