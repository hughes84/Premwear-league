"""
Module for registering models with the Django admin site.
"""
from django.contrib import admin
from .models import WishList

# Register your models here.

admin.site.register(WishList)
