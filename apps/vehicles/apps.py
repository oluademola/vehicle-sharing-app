"""
This module contains Vehicle model config option
"""

from django.apps import AppConfig


class VehiclesConfig(AppConfig):
    """
    Defines auto filed ID value for the Vehicle model
    """
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.vehicles"
