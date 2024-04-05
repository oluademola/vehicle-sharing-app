"""
This module contains vehicle config options
"""

from django.db import models


class VehicleManager(models.Manager):
    """
    This class contains methods for querying vehicle.
    """
    def total_vehicles_available_for_rent(self):
        """
        get and returns total vehicle available
        """
        return self.get_queryset().filter(availability_status=True).count()

    def total_vehicles_added_by_user(self, user_id):
        """
        get vehicles added by user
        """
        return self.get_queryset().filter(owner_id=user_id).count()
