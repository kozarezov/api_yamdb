from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from users.models import User


class UserSignUpSerializer(serializers.ModelSerializer):
    """Сериализация данных при регистрации пользователя."""

    username = serializers.CharField(
        max_length=150,
        required=True,
        validators=[UniqueValidator(
            queryset=User.objects.all(),
            message='Пользователь с таким username уже существует')]
    )
    email = serializers.EmailField(
        max_length=254,
        required=True,
        validators=[UniqueValidator(
            queryset=User.objects.all(),
            message='Пользователь с таким email уже существует')]
    )

    class Meta:
        model = User
        fields = ('email', 'username')

    def validate_username(self, value):
        if value == "me":
            raise serializers.ValidationError(
                'Невозможно создать пользователя с логином me'
            )
        return value


class TokenSerializer(serializers.Serializer):
    """Сериализация токена."""

    username = serializers.CharField(max_length=150)
    confirmation_code = serializers.CharField()


class UsersSerializer(serializers.Serializer):
    """Сериализация модели User."""

    class Meta:
        model = User
        fields = ('username', 'email',
                  'first_name', 'last_name',
                  'bio', 'role')
