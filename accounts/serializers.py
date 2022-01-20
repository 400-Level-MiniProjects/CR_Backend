from curses.ascii import US
from dataclasses import field
from rest_framework import serializers
from .models import *
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'date_joined',)

class UserSerialization(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'first_name', 'last_name',)
        extra_kwargs = {'password': {'write_only': True}}

        def create(self, validated_data):

            user = User(
                email=validated_data['email'],
                first_name = validated_data['first_name'],
                last_name = validated_data['last_name'],
            )

            user.set_password(validated_data['password'])
            user.save()

            return user