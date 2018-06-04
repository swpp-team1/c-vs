from rest_framework import permissions
from cvs_rest.models import Comment

class IsOwnerOrReadOnly(permissions.BasePermission):
    message = 'You are not the owner'
    """
    def has_permission(self, request, view):
        print(request)
        print(view.kwargs)
        owner = Comment.objects.get(id=view.kwargs['pk'])
        print(owner.user_id)
        return False
        if request.method in permissions.SAFE_METHODS:
            return True
        owner = Comment.objects.get(id=view.kwargs['pk'])
        return obj.user_id == request.user and (not request.user.is_anonymous)
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user_id == request.user.id
