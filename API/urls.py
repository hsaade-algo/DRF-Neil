"""This file contains all the API Endpoints"""

from django.urls import path
from rest_framework import routers
from django.conf.urls import url, include

from .views import (
    UserLoginApiView,
    FooViewSet,
    FooBarViewSet
)

# URL Router to register and route the ModelViewSet Endpoints 
router = routers.SimpleRouter()

router.register(
    'foo',
    FooViewSet,
    basename='foo'
)

router.register(
    'foobar',
    FooBarViewSet,
    basename='foobar'
)

urlpatterns = [
    path('login/', UserLoginApiView.as_view(), name='login'),
    url('', include(router.urls))
]
