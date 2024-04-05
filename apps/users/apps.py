"""
This module contains Booking model config option.
"""

from django.apps import AppConfig


class UsersConfig(AppConfig):
    """
    Defines auto filed ID value for the User model
    """
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.users"
