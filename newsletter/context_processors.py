"""
Module for importing the NewsletterSubscriptionForm from the current directory's forms module.
"""
from .forms import NewsletterSubscriptionForm


def newsletter_form(request):
    """
    Get Newsletter Form

    Returns a dictionary containing the newsletter form.

    Returns:
        dict: A dictionary containing the newsletter form.
    """
    return {"newsletter_form": NewsletterSubscriptionForm()}
