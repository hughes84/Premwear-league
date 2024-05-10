"""
Module for interacting with the Django ORM (Object-Relational Mapping) system.
"""
from django.db import models


class Category(models.Model):
    """
    Represents a category for products in the store.

    """

    class Meta:
        """
        Meta class configuration for the Category model.
        Sets the plural name for the model in the admin interface.
        """
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def _str_(self):
        return self.name

    def get_friendly_name(self):
        """
        Method to get the friendly name of the category.
        """
        return self.friendly_name


class Product(models.Model):
    """
    Represents product in store.

    """

    category = models.ForeignKey(
        "Category", null=True, blank=True, on_delete=models.SET_NULL
    )
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
