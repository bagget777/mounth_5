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
    
class CoursesView(TemplateView):
    template_name = 'posts/courses.html'

class BackendView(TemplateView):
    template_name = 'courses/backend.html'

class FrontendView(TemplateView):
    template_name = 'courses/frontend.html'
    
class FullstackView(TemplateView):
    template_name = 'courses/fullstack.html'
    
class AndroidView(TemplateView):
    template_name = 'courses/android.html'
    
class IOSView(TemplateView):
    template_name = 'courses/ios.html'

class UXUIView(TemplateView):
    template_name = 'courses/uxui.html'




