from django.shortcuts import render
from django.http import HttpResponse, request
from django.views import generic
from .models import *
from django.views.generic import TemplateView

class IndexView(generic.ListView):
    model = Post
    template_name = "index.html"
    context_object_name = "posts"

class AboutView(TemplateView):
    template_name = 'posts/About.html'
    
class FAQView(TemplateView):
    template_name = 'posts/faq.html'





