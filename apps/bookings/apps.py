"""
Booking model configuration
"""

from django.apps import AppConfig


class BookingsConfig(AppConfig):
    """
    Defined booking model config for ID
    """
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.bookings"
