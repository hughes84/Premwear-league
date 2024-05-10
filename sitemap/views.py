"""
Module for handling views related to sitemaps and categories.
"""
from django.shortcuts import render
from django.views.decorators.http import require_GET
from premwear_league.urls import sitemaps
from products.models import Category

# pylint: disable=no-member


@require_GET
def sitemap_html(request):
    """
    Render the HTML sitemap page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered sitemap page.
    """
    urls = {}

    for key, value in sitemaps.items():
        sitemap_class = value()
        sitemap_urls = sitemap_class.get_urls()
        urls[key] = []
        for sitemap_item in sitemap_urls:
            urls[key].append((sitemap_item["item"], sitemap_item["location"]))
    categories = Category.objects.all()

    context = {"urls": urls, "categories": categories}
    return render(request, "sitemap.html", context)
