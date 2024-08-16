from rest_framework import permissions


class IsActiveUser(permissions.BasePermission):
    """Разрешение, которое позволяет доступ только активным пользователям."""

    def has_permission(self, request, view):
        """Разрешает доступ только если пользователь аутентифицирован и активен"""
        return request.user and request.user.is_authenticated and request.user.is_active
