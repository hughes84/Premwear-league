"""
URL configuration for contact-related views.
"""
from django.urls import path
from .views import contact_us

urlpatterns = [
    path("", contact_us, name="contact_us"),
]
