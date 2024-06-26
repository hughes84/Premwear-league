"""
Module for working with Django forms.
"""
from django import forms


class NewsletterSubscriptionForm(forms.Form):
    """
    Newsletter Subscription Form

    A simple form for capturing email
    addresses for newsletter subscriptions.
    """

    email = forms.EmailField(
        label="Email:", widget=forms.TextInput(
            attrs={"id": "email_newsletter"})
    )
