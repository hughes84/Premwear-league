"""
Module for accessing application configuration settings.
"""
from django.apps import AppConfig


class BagConfig(AppConfig):
    """
    AppConfig for the bag app.
    """
    default_auto_field = "django.db.models.BigAutoField"
    name = "bag"
