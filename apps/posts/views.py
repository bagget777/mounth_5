from django.shortcuts import render
from django.views import generic
from .models import *
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from .forms import EnrollmentForm

def enroll_view(request):
    if request.method == 'POST':
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('enroll_success')
    else:
        form = EnrollmentForm()
    return render(request, 'courses/enroll.html', {'form': form})


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




