"""
Module for importing settings and S3 storage backend for Django.
"""
from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    """
    Custom static file storage class using S3Boto3Storage.
    Sets the location to the STATICFILES_LOCATION from settings.
    """
    location = settings.STATICFILES_LOCATION


class MediaStorage(S3Boto3Storage):
    """
    Custom media file storage class using S3Boto3Storage.
    Sets the location to the MEDIAFILES_LOCATION from settings.
    """
    location = settings.MEDIAFILES_LOCATION
    