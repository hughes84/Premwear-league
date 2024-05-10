"""
    Configuration app for the contact form.
    """
from django.apps import AppConfig


class ContactConfig(AppConfig):
    """
    AppConfig for the contact app.
    """
    default_auto_field = "django.db.models.BigAutoField"
    name = "contact"
