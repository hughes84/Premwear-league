"""
Module for working with Django models.
"""
from django.db import models


class About(models.Model):
    """
    Model representing information about the company or organization.
    """
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to="about_images/", null=True, blank=True)

    def _str_(self):
        return self.title
