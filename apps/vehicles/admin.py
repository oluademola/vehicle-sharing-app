"""
This contains admin view and customisation options
for the users module.
"""

from django.contrib import admin

from .models import Vehicle


@admin.register(Vehicle)
class AdminVehicle(admin.ModelAdmin):
    """
    list display option
    """
    list_display = ('id', 'owner', 'vehicle_type', 'vehicle_make', 'model', 'year',
    'get_max_speed', 'get_price_per_hr', 'availability_status')
    readonly_fields = ('id',)

    def get_max_speed(self, obj):
        """
        get max speed
        """
        return f"{obj.max_speed} km/hr"
    get_max_speed.short_description = "max speed"

    def get_price_per_hr(self, obj):
        """
        get price
        """
        return f"${obj.price_per_hour}"
    get_price_per_hr.short_description = "price per hour"
