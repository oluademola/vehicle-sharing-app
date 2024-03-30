"""
A brief description of the module's functionality.
"""

from django.shortcuts import redirect
from django.contrib import messages
from django.views import generic
from django.db.models import Q
from apps.vehicles.models import Vehicle
from apps.common.choices import VEHICLE_MAKES, VEHICLE_TYPES


class HomeView(generic.ListView):
    """
    A brief description of the class functionality.
    """
    model = Vehicle
    template_name = "home.html"
    context_object_name = "vehicles"
    paginate_by = 20

    def get_context_data(self, **kwargs):
        """
        A brief description of the method functionality.
        """
        context = super().get_context_data(**kwargs)
        context["VEHICLE_MAKES"] = VEHICLE_MAKES
        context["VEHICLE_TYPES"] = VEHICLE_TYPES
        context["total_available_vehicles"] = self.get_queryset().count()
        return context


class AboutView(generic.TemplateView):
    """
    A brief description of the class functionality.
    """
    template_name = "about.html"
