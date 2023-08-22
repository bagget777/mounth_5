from .views import IndexView, AboutView, FAQView, CoursesView, BackendView, FrontendView, FullstackView, AndroidView, IOSView, UXUIView, enroll_view
from django.urls import path

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("about/", AboutView.as_view(), name="about"),
    path("faq/", FAQView.as_view(), name="faq"),
    path("courses/", CoursesView.as_view(), name="courses"),
    path("backend/", BackendView.as_view(), name="backend"),
    path("frontend/", FrontendView.as_view(), name="frontend"),
    path("fullstack/", FullstackView.as_view(), name="fullstack"),
    path("android/", AndroidView.as_view(), name="android"),
    path("ios/", IOSView.as_view(), name="ios"),
    path("uxui/", UXUIView.as_view(), name="uxui"),
    path('enroll/', enroll_view, name='enroll'),
]
