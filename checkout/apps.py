"""
Configuration for the checkout app.
"""
from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    """
    AppConfig for the checkout app.
    """
    name = "checkout"

    def ready(self):
        """
        Method called when the application is ready.
        Imports signals to ensure they are loaded.
        """
        import checkout.signals
