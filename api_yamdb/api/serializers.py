from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from reviews.models import Category, Genre, Title
from users.models import User


class CategorySerializer(serializers.ModelSerializer):
    """Сериализация модели Category."""

    class Meta:
        model = Category
        fields = ('name', 'slug')


class GenreSerializer(serializers.ModelSerializer):
    """Сериализация модели Genre."""

    class Meta:
        model = Genre
        fields = ('name', 'slug')


class TitleSerializer(serializers.ModelSerializer):
    """Сериализация модели Title."""
    genre = serializers.SlugRelatedField(queryset=Genre.objects.all(),
                                         many=True, slug_field='slug')
    category = serializers.SlugRelatedField(queryset=Category.objects.all(),
                                            slug_field='slug')

    class Meta:
        model = Title
        fields = '__all__'


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
