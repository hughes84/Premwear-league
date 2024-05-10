"""
Module for accessing application configuration settings.
"""
from django.apps import AppConfig


class SitemapConfig(AppConfig):
    """
    AppConfig for the sitemap app.
    """
    default_auto_field = "django.db.models.BigAutoField"
    name = "sitemap"
