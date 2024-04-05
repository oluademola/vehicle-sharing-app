"""
This module contains Vehicle model configurations.
"""

from django.db import models
from django.urls import reverse
from apps.common.base_model import BaseModel
from apps.common import choices
from apps.users.models import CustomUser
from apps.vehicles.managers import VehicleManager


class Vehicle(BaseModel):
    """
    Vehicle model class.
    """
    owner = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="vehicle")
    vehicle_type = models.CharField(
        choices=choices.VEHICLE_TYPES, max_length=100, blank=True, null=True)
    vehicle_make = models.CharField(
        choices=choices.VEHICLE_MAKES, max_length=100, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)
    year = models.CharField(max_length=50, blank=True, null=True)
    max_speed = models.CharField(max_length=10, blank=True, null=True)
    total_doors = models.CharField(
        max_length=20, choices=choices.TOTAL_VEHICLE_DOORS, blank=True, null=True)
    transmission_type = models.CharField(
        max_length=50, choices=choices.TRANSMISSION_TYPES, blank=True, null=True)
    total_passengers = models.CharField(
        max_length=20, choices=choices.TOTAL_PASSENGERS, blank=True, null=True)
    registration_certificate = models.FileField(
        upload_to="vehicle certificates/", blank=True, null=True)
    fuel_type = models.CharField(
        max_length=50, choices=choices.FUEL_TYPE,  blank=True, null=True)
    temperature_regulator = models.CharField(
        max_length=50, choices=choices.TEMPERATURE_REGULATOR, default="Air Conditioning")
    engine_capacity = models.CharField(max_length=50, blank=True, null=True)
    availability_status = models.CharField(
        max_length=50, choices=choices.AVAILABILITY_STATUS, default="Available")
    price_per_hour = models.DecimalField(
        max_digits=10, decimal_places=2,  blank=True, null=True)
    pickup_location = models.CharField(max_length=150, blank=True, null=True)
    image = models.ImageField(
        upload_to="vehicle images/", blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    objects = VehicleManager

    class Meta:
        """
        metadata options
        """
        indexes = [
            models.Index(fields=['vehicle_type']),
            models.Index(fields=['vehicle_make']),
        ]
        verbose_name = "Vehicle"
        verbose_name_plural = "Vehicles"

    def __str__(self):
        """
        return instance of the vehicle.
        """
        return f"{self.vehicle_make} {self.vehicle_type}"

    def get_absolute_url(self):
        """
        get absolute URL of vehicle details page
        """
        return reverse("vehicle_detail", kwargs={"id": self.id})

    def get_total_passengers(self):
        """
        gets and return number of seat
        """
        return f"{self.total_passengers} Passengers"

    def get_total_doors(self):
        """
        gets and returns number of vehicle doors
        """
        return f"{self.total_doors} Doors"

    def get_max_speed(self):
        """
        returns max speed
        """
        return f"{self.max_speed} km/hr"

    def get_price_per_hour(self):
        """
        return price
        """
        return f"${self.price_per_hour}/hr"

    def get_full_vehicle_name(self):
        """
        returns a capitalization of vehicle name
        """
        return f"{self.vehicle_make.capitalize()} {self.vehicle_type.capitalize()} {self.model.capitalize()}"
