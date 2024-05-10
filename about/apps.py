"""
Module for accessing application configuration settings.
"""
from django.apps import AppConfig


class AboutConfig(AppConfig):
    """
    Configuration class for the 'about' app.
    """
    default_auto_field = "django.db.models.BigAutoField"
    name = "about"
