from django.db import models
from rest_framework import fields, serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User
        fields = '__all__'



class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

        def create(self, validated_data):
            new_user = User.objects.create_user(**validated_data)
            return new_user


class LoginSerializer(serializers.Serializer):
    class Meta:
        username = serializers.CharField()
        password = serializers.CharField(write_only=True)

        def validate(self, data):
            user = authenticate(**data)
            if user and user.is_active:
                return user
            raise serializers.ValidationError('wrong_credentials')
