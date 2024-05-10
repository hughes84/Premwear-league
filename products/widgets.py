"""
Module for importing widgets and translation utilities for forms.
"""
from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _


class CustomClearableFileInput(ClearableFileInput):
    """
    Custom file input widget with clearable functionality.
    """
    clear_checkbox_label = _("Remove")
    initial_text = _("Current Image")
    input_text = _("")
    template_name = "products/custom_widget_templates/custom_clearable_file_input.html"
