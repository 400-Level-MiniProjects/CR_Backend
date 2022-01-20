from django.shortcuts import render

from rest_framework import permissions
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status

from knox.models import AuthToken

from .serializers import *
# Create your views here.

class RegisterUser(GenericAPIView):
    serializer_class = UserSerialization

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            return Response(
                {
                    "user": UserSerializer(user, context=self.get_serializer_context()).data,
                    "token": AuthToken.objects.create(user)[1]
                }, status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)