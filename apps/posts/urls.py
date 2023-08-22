from .views import IndexView, AboutView, FAQView, CoursesView
from django.urls import path

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("about/", AboutView.as_view(), name="about"),
    path("faq/", FAQView.as_view(), name="faq"),
    path("courses/", CoursesView.as_view(), name="courses")
]
