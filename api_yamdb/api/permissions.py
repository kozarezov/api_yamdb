from rest_framework import permissions


class IsAdmin(permissions.BasePermission):
    """Проверка, что пользователь является админом."""

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_admin
