from rest_framework import permissions


class IsAdmin(permissions.BasePermission):
    """Проверка, что пользователь является админом."""

    message = 'У Вашей учетной записи недостаточно прав (ADMIN)'

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_admin


class IsAdminOrReadOnly(permissions.BasePermission):
    """Проверка, что пользователь является админом или применен безопасный
    метод."""
    message = 'У Вашей учетной записи недостаточно прав (ADMIN)'

    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                or (request.user.is_authenticated and request.user.is_admin))


class IsAuthorOrAdminOrModerator(permissions.BasePermission):
    """Проверка, что пользователь является админом, автором отзыва,
    модератором или применен безопасный
     метод."""

    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or obj.author == request.user
                or request.user.is_moderator
                or request.user.is_admin)
