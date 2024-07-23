from rest_framework.permissions import BasePermission


class IsGuide(BasePermission):
    def has_permission(self, request, view):
        return request.user and hasattr(request.user, 'guideapplication') and request.user.guideapplication.is_approved
