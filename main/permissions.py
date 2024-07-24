from rest_framework import permissions


class IsAdminOrGuide(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated:
            if request.user.is_staff:
                return True
            if hasattr(request.user, 'guideapplication') and request.user.guideapplication.is_approved:
                if request.method in permissions.SAFE_METHODS or request.method in ['PUT', 'PATCH', 'DELETE']:
                    return True
            if request.method in permissions.SAFE_METHODS:
                return True

        return False

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user
