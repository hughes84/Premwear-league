from django.db import models
from django.contrib.auth.models import User

class ContactUs(models.Model):
    message = models.TextField()
    name = models.CharField(max_length=100)
    email = models.EmailField()
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Contact Us Form - {self.email}"
