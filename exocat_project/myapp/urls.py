from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),  # Give about its own URL
    path("data/", views.about, name="data")
]