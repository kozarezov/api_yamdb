from django.db import models


class Category(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=100)
    slug = models.SlugField(verbose_name='Слаг', max_length=20, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('name',)


class Genre(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=100)
    slug = models.SlugField(verbose_name='Слаг', max_length=20, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
        ordering = ('name',)


class Title(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=100)
    year = models.IntegerField(verbose_name='Дата релиза')
    description = models.TextField(verbose_name='Описание', null=True,
                                   blank=True)
    genre = models.ManyToManyField(Genre, through='TitleGenre',
                                   on_delete=models.SET_NULL,
                                   verbose_name='Жанр')
    category = models.ForeignKey(Category, related_name='titles',
                                 on_delete=models.SET_NULL, null=True,
                                 verbose_name='Категория')
    rating = models.IntegerField(verbose_name='Рейтинг', null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'
        ordering = ('name',)


class TitleGenre(models.Model):
    title = models.ForeignKey(Title, verbose_name='Произведение',
                              on_delete=models.SET_NULL)
    genre = models.ForeignKey(Genre, verbose_name='Жанр',
                              on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.title} (жанр - {self.genre})'

    class Meta:
        verbose_name = 'Произведение и жанр'
        verbose_name_plural = 'Произведения и жанры'
