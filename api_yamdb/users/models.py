from django.contrib.auth.models import AbstractUser
from django.db import models

USER = 'User'
MODERATOR = 'Moderator'
ADMIN = 'Admin'

ROLES = (
    (USER, 'Пользователь'),
    (MODERATOR, 'Модератор'),
    (ADMIN, 'Администратор'),
)


class User(AbstractUser):
    """Кастомная модель User."""

    username = models.CharField('Логин', max_length=150, unique=True)
    email = models.EmailField('Email', max_length=254, unique=True)
    first_name = models.CharField('Имя', max_length=150, blank=True)
    last_name = models.CharField('Фамилия', max_length=150, blank=True)
    bio = models.TextField('Информация о себе', blank=True)
    role = models.CharField('Роль', max_length=15, choices=ROLES, default=USER)
