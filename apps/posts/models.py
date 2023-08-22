from django.db import models
from django.contrib.auth.models import User

from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(default='100')
    cover = models.ImageField(upload_to='post_covers/')
    status = models.CharField(max_length=20, choices=[('draft', 'Draft'), ('published', 'Published')])  # Добавляем поле status

    def __str__(self):
        return self.title


class Enrollment(models.Model):
    course_name = models.CharField(max_length=200)
    user_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.course_name


        
        
