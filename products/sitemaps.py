from .models import Product
from django.contrib.sitemaps import Sitemap

class ProductSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return Product.objects.all()

    # def lastmod(self, obj):
    #     return obj.updated_at

    def location(self, item):
        """
        Returns the URL location for a given product in the sitemap.

        Args:
        - item (Product): The product for which to generate the URL.

        Returns:
        - str: The URL location for the product in the sitemap.

        Note:
        Modify this based on your URL structure.
        """
        return f'/products/{item.id}/'
