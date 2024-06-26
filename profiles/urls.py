"""
Module for defining URL patterns for the app's views.
"""
from django.urls import path
from . import views

urlpatterns = [
    path("", views.profile, name="profile"),
    path("order_history/<order_number>",
         views.order_history, name="order_history"),
    path("add_to_wishlist/<product_id>",
         views.add_to_wishlist, name="add_to_wishlist"),
]
