from rest_framework import permissions


class IsAdmin(permissions.BasePermission):
    """Проверка, что пользователь является админом."""

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_admin


class IsAdminOrReadOnly(permissions.BasePermission):
    """Проверка, что пользователь является админом или применен безопасный
    метод."""

    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS or
                (request.user.is_authenticated and request.user.is_admin))
