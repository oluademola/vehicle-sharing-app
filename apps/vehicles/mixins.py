"""
Module contains basic filtering option for vehicle object.
"""

class VehicleOwnerMixing:
    """
    Handles filtered query by user
    """
    def get_queryset(self):
        """
        Get query set 
        """
        return self.get_queryset().filter(owner=self.request.user)
