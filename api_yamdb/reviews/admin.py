from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import Category, Genre, Title, TitleGenre, Comment, Review


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
    
@admin.register(Comment)
class CommentAdmin(ImportExportModelAdmin):
    list_display = (
        'review',
        'text',
        'author',
        'pub_date',
    )
    search_fields = ('review',)
    list_filter = ('review',)
    empty_value_display = '-пусто-'
    
@admin.register(Review)
class ReviewAdmin(ImportExportModelAdmin):
    list_display = (
        'title',
        'text',
        'author',
        'score',
    )
    search_fields = ('pub_date',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'
