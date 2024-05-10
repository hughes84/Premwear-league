"""
Module for working with forms, widgets, and models related to products.
"""
from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category

# pylint: disable=no-member


class ProductForm(forms.ModelForm):
    """
    Form for creating and updating product instances.
    """

    class Meta:
        """
        Meta class configuration for the ProductForm.
        """
        model = Product
        fields = "__all__"

    image = forms.ImageField(
        label="Image", required=False, widget=CustomClearableFileInput
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields["category"].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "border-black rounded-0"
