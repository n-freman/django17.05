from django.contrib import admin

from .models import Book


class BookAdminConfig(admin.ModelAdmin):
    list_display = ['title', 'owner', 'created_at']


admin.site.register(Book, BookAdminConfig)
