from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from .serializers import *

# from django.contrib.auth.models import User
from django.contrib.auth import login

# Create your views here.


class RegistrationView(GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serialized_data = self.get_serializer(data=request.data)
        serialized_data.is_valid(raise_exception=True)

        # Saving the user 
        user = serialized_data.save()

        # Logging in User after registeration
        login(request=request, user=user)

        # De-serialization
        user_data = UserSerializer(user, context=self.get_serializer_context()).data

        return Response({'user_data': user_data})


class LoginView(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serialized_data = self.get_serializer(data=request.data)
        serialized_data.is_valid(raise_exception=True)

        # User Data
        user = serialized_data.validated_data

        # Login the user
        login(request=request, user=user)

        # De-Serialization
        user_data = UserSerializer(user, context=self.get_serializer_context()).data

        return Response({'user_data': user_data})
