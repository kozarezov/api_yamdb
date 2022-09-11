from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from .validators import validate_year

User = get_user_model()


class Category(models.Model):
    """Категория произведения."""
    name = models.CharField(verbose_name='Имя', max_length=100)
    slug = models.SlugField(verbose_name='Слаг', max_length=100, unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('name',)

    def __str__(self):
        return self.name


class Genre(models.Model):
    """Жанр произведения."""
    name = models.CharField(verbose_name='Имя', max_length=100)
    slug = models.SlugField(verbose_name='Слаг', max_length=100, unique=True)

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
        ordering = ('name',)

    def __str__(self):
        return self.name


class Title(models.Model):
    """Произведение (книга, фильм, муз. композиция)."""
    name = models.CharField(verbose_name='Имя', max_length=100)
    year = models.IntegerField(verbose_name='Дата релиза',
                               validators=(validate_year,))
    description = models.TextField(verbose_name='Описание', null=True,
                                   blank=True)
    genre = models.ManyToManyField(Genre, through='TitleGenre',
                                   verbose_name='Жанр')
    category = models.ForeignKey(Category, related_name='titles',
                                 on_delete=models.SET_NULL, null=True,
                                 verbose_name='Категория')

    class Meta:
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'
        ordering = ('name',)

    def __str__(self):
        return self.name


class TitleGenre(models.Model):
    """Модель для определения нескольких жанров у произведений."""
    title = models.ForeignKey(Title, verbose_name='Произведение',
                              on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, verbose_name='Жанр',
                              on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} (жанр - {self.genre})'

    class Meta:
        verbose_name = 'Произведение и жанр'
        verbose_name_plural = 'Произведения и жанры'


class Review(models.Model):
    """Модель отзывов."""
    text = models.TextField(verbose_name='Текст отзыва')
    title = models.ForeignKey(Title, verbose_name='Произведение',
                              on_delete=models.CASCADE, related_name='reviews')
    score = models.IntegerField(validators=[MinValueValidator(limit_value=1),
                                MaxValueValidator(
                                    limit_value=10)], verbose_name='Оценка',
                                                                   null=True)
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE, verbose_name='Автор отзыва')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        constraints = [
            models.UniqueConstraint(fields=('title', 'author'),
                                    name='unique_review')
        ]
        ordering = ('-pub_date',)


class Comment(models.Model):
    """Модель комментариев."""
    text = models.TextField(max_length=200,
                            verbose_name='Комментарий к отзыву')
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE, verbose_name='Автор комментария')
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    review = models.ForeignKey(Review, on_delete=models.CASCADE,
                               related_name='comments')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
