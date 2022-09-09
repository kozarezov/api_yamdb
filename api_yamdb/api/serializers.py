from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from reviews.models import Category, Genre, Title, Review, Comment
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
    rating = serializers.IntegerField(source='reviews__score__avg',
                                      read_only=True)

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


class UsersSerializer(serializers.ModelSerializer):
    """Сериализация модели User."""

    class Meta:
        model = User
        fields = ('username', 'email',
                  'first_name', 'last_name',
                  'bio', 'role')


class UsersMeSerializer(serializers.ModelSerializer):
    """Сериализация модели User."""

    class Meta:
        model = User
        fields = ('username', 'email',
                  'first_name', 'last_name',
                  'bio', 'role')
        read_only_fields = ('role',)


class ReviewSerializer(serializers.ModelSerializer):
    """Сериализация модели Review."""
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username')

    score = serializers.IntegerField(max_value=10, min_value=1)
    title = Title.objects.get(id=self.kwargs.get('title_id')) # НЕ СРАБОТАЕТ?

    class Meta:
        model = Review
        fields = ('text', 'title', 'score', 'pub_date' 'author')

    def validate_review(self, request):
        if self.context['request'].method == 'POST':
            if Review.objects.filter(
                    author=self.context['request'].user).exists:
                raise serializers.ValidationError(
                    'Можно оставить только один отзыв на произведение')
        return request

    def validate_integer_number(self, score):
        if score > 10 or score < 1:
            raise serializers.ValidationError(
                'Выберете оценку от 1 до 10')


class CommentSerializer(serializers.ModelSerializer):
    """Сериализация модели Comment."""

    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
    )

    class Meta:
        fields = '__all__'
        model = Comment
        read_only_fields = ('review',)
