"""
Module contains basic filtering option for booking.
"""

class BookingMixing:
    """
    This class contains filtering option on how bookings 
    info are returned on the renter and owner's view.
    """
    def get_queryset(self):
        """
        This methods returns query associated with either renter or owner
        """
        queryset = self.get_queryset()
        if queryset.filter(renter=self.request.user):
            return queryset
        return queryset.filter(vehicle__owner=self.request.user)
