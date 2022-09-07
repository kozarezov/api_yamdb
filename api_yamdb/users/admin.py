from import_export.admin import ImportExportModelAdmin
from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(ImportExportModelAdmin):
    """Настройки админ панели для User."""

    list_display = ('pk', 'username',
                    'email', 'first_name',
                    'last_name', 'role')
    search_fields = ('username',)
    list_filter = ('role',)
    empty_value_display = '-пусто-'
