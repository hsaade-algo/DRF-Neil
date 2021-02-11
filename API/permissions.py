from rest_framework import permissions


class FooPermission(permissions.BasePermission):
    """Custom Permission Class for Foo Model """

    def has_permission(self, request, view):
        if request.user and (request.user.is_superuser or request.user.is_staff):
            return True

        if request.user and request.user.groups.filter(name="FooGroup"):
            return True
        return False

class FooBarPermission(permissions.BasePermission):
    """Custom Permission Class for FooBar Model """
    
    def has_permission(self, request, view):
        if request.user and (request.user.is_superuser or request.user.is_staff):
            return True

        if (request.user
            and request.method in permissions.SAFE_METHODS
            and request.user.groups.filter(name="FooBarGroup")):
            return True
        return False
