from rest_framework import permissions
from rest_framework.compat import is_authenticated


class IsOwnerorReadonly(permissions.BasePermission):
    message = 'You are not the owner'

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.user_id == request.user and is_authenticated(request.user)

