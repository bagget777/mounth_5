from django.db import models

class Post(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовка"
    )
    context = models.TextField(
        verbose_name="Описаение"
    )
    created = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата создание"
    )
    status = models.BooleanField(
        default=True, 
        verbose_name="Статус публикации"
    )
    cover = models.ImageField(
        default="image.jpg", 
        upload_to="uploads/posts", 
        blank=True, 
        verbose_name="Обложка"
    )
    
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        
        
