from django.contrib.auth.models import AbstractUser
from django.db import models


USER = 'User'
MODERATOR = 'Moderator'
ADMIN = 'Admin'

ROLES = (
    (USER, 'Пользователь'),
    (MODERATOR, 'Модератор'),
    (ADMIN, 'Админ'),
)


class User(AbstractUser):
    bio = models.TextField(
        'Биография',
        blank=True,
    )
    role = models.CharField(
        max_length=15,
        choices=ROLES,
        default=USER
    )
