from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsUserOwnerOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        return request.user.is_superuser or request.user.is_staff

class IsCommentsOwnerOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        elif request.method == 'DELETE':
            return obj.owner == request.user or obj.books.owner == request.user
        return obj.owner == request.user