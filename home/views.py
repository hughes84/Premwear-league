"""
Module for rendering views related to product ratings.
"""
from django.shortcuts import render
from django.db.models import Avg
from products.models import Product

# pylint: disable=no-member


def index(request):
    """A view to return the index page"""

    # Query top-rated products with average rating greater than or equal to 3
    top_rated_products = Product.objects.annotate(avg_rating=Avg("rating"))\
        .filter(
        avg_rating__gte=3
    )
    return render(request, "home/index.html", {"rated": top_rated_products})
