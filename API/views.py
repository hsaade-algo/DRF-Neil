# Module Import
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework import authentication, permissions

# Models Import
from Data.models import Foo, FooBar

# Serializers Import
from .serializers import (
    FooSerializer,
    FooBarSerializer
)

# Importing Custom Permissions
from .permissions import FooPermission, FooBarPermission

class UserLoginApiView(ObtainAuthToken):
    """Handles creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class FooViewSet(viewsets.ModelViewSet):
    """Endpoint for Foo Model"""
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsAuthenticated, FooPermission]
    queryset = Foo.objects.all()
    serializer_class = FooSerializer


class FooBarViewSet(viewsets.ModelViewSet):
    """Endpoint for Foobar Model"""
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsAuthenticated, FooBarPermission]
    queryset = FooBar.objects.all()
    serializer_class = FooBarSerializer
