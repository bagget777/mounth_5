from django.shortcuts import render
from django.http import HttpResponse, request
from django.views import generic
from .models import *

class IndexView(request):
    model = Post
    template_name = "index.html"
    context_object_name = "posts"

class AboutView(request):
    template_name = 'posts/About.html'




