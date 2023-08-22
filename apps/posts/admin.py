from django.contrib import admin
from .models import Post  # Используйте относительный импорт

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "created_at", "status"]  # Замените "created" на "created_at"
    list_filter = ["status"]
    list_editable = ["status"]
