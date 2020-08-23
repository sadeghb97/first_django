from django.contrib.auth.models import User
from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True

        try:
            user = User.objects.get(username=request.query_params['username'])
            if request.user == user:
                return True
            return False
        except:
            return False
