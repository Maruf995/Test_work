from rest_framework import serializers
from django.core.exceptions import ValidationError

from .models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, min_length=8)
    is_author = serializers.BooleanField(required=False)
    is_subscriber = serializers.BooleanField(required=False)

    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'is_author', 'is_subscriber']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['email'],
            is_author=validated_data.get('is_author', False),
            is_subscriber=validated_data.get('is_subscriber', True)
        )
        user.set_password(validated_data['password'])
        user.save()
        return user