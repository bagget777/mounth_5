from django import forms
from apps.posts.models import Post
from .models import Enrollment

class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ['course_name', 'user_name', 'email', 'phone_number']
        
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'cover') 