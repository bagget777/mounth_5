from django.contrib import admin
from .models import Post  # Импорт вашей модели

@admin.register(Post)  # Регистрация модели с использованием декоратора
class PostAdmin(admin.ModelAdmin):
    list_display = ["title","status"]
    list_filter = ["status"]
    list_editable = ["status"]
