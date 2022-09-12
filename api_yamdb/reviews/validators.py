from django.core.exceptions import ValidationError
from django.utils import timezone


def validate_year(value):
    if value > timezone.now().year:
        raise ValidationError('Некорректное значение года релиза: год не '
                              'может быть больше текущего!')
