"""
This is the main application or core view that contains 
the general logic of the homepage, about view and search.
"""
from django.db.models import Q
from django.views import generic
from apps.vehicles.models import Vehicle
from apps.common.choices import VEHICLE_MAKES, VEHICLE_TYPES


class HomeView(generic.ListView):
    """
    This class contains the logic to list vehicles based on certain search query
    """
    model = Vehicle
    template_name = "home.html"
    context_object_name = "vehicles"
    paginate_by = 20

    def get_queryset(self):
        """
        This method gets and returns a list of vehicles based on a query set
        """
        queryset = super().get_queryset()
        vehicle_make_query = self.request.GET.get("vehicle_make")
        vehicle_type_query = self.request.GET.get("vehicle_type")

        if vehicle_make_query:
            qs = queryset.filter(vehicle_make__iexact=vehicle_make_query)
            return qs

        if vehicle_type_query:
            qs = queryset.filter(vehicle_type__iexact=vehicle_type_query)
            return qs

        if vehicle_make_query and vehicle_make_query:
            chained_qs = (
                Q(vehicle_make__iexact=vehicle_make_query) & 
                Q(vehicle_type__iexact=vehicle_type_query)
            )
            qs = queryset.filter(chained_qs)
            return qs if qs else None

        return queryset

    def get_context_data(self, **kwargs):
        """
        This method is responsible for rendering prefilled options
        in the template.
        """
        context = super().get_context_data(**kwargs)
        context["VEHICLE_MAKES"] = VEHICLE_MAKES
        context["VEHICLE_TYPES"] = VEHICLE_TYPES
        context["total_available_vehicles"] = self.get_queryset().count()
        return context


class AboutView(generic.TemplateView):
    """
    This class or view renders the "About" page.
    """
    template_name = "about.html"
