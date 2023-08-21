from django.shortcuts import render
from django.views import generic
from .models import *

class IndexView(generic.ListView):
    # model = Post
    queryset = Post.objects.all()
    template_name = "index.html"
    # context_object_name = "posts"


