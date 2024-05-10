"""
Module for defining URL patterns for the app's views.
"""
from django.urls import path
from .views import about

urlpatterns = [
    path("", about, name="about"),
]
