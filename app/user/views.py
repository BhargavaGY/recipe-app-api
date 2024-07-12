"""Views for User APIs"""

from rest_framework import generics

from .serializers import UserSerializer


class CreateUserView(generics.CreateAPIView):
    """View to create new user"""
    serializer_class = UserSerializer
