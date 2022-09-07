from import_export.admin import ImportExportModelAdmin
from django.contrib import admin

from .models import Category, Genre, Title, TitleGenre


@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    list_display = (
        'id',
        'name',
        'slug'
    )
    empty_value_display = '-пусто-'


@admin.register(Genre)
class GenreAdmin(ImportExportModelAdmin):
    list_display = (
        'id',
        'name',
        'slug'
    )
    empty_value_display = '-пусто-'


@admin.register(Title)
class TitleAdmin(ImportExportModelAdmin):
    list_display = (
        'id',
        'name',
        'year',
        'description',
        'category',
    )
    empty_value_display = '-пусто-'


@admin.register(TitleGenre)
class TitleGenreAdmin(ImportExportModelAdmin):
    list_display = (
        'id',
        'title',
        'genre',
    )
    empty_value_display = '-пусто-'
