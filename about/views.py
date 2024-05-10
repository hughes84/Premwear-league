"""
Module for rendering templates in Django views.
"""
from django.shortcuts import render

# Create your views here.
def about(request):
    """
    Render the about us page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered about us page.
    """
    return render(request, 'about.html')
