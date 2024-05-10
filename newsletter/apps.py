"""
Module for accessing application configuration settings.
"""
from django.apps import AppConfig


class NewsletterConfig(AppConfig):
    """
    AppConfig for the newsletter app.
    """
    default_auto_field = "django.db.models.BigAutoField"
    name = "newsletter"
