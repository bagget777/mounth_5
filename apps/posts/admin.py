from django.contrib import admin
from apps.posts.models import Post

# admin.site.register(Post)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "created", "status"]
    list_filter = ["status"]
    list_editable = ["status"]