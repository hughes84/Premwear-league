"""
Module for accessing application configuration settings.
"""
from django.apps import AppConfig


class ProductsConfig(AppConfig):
    """
    AppConfig for the products app.
    """
    default_auto_field = "django.db.models.BigAutoField"
    name = "products"
