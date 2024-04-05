"""
This module contains booking forms config.
"""

from django import forms
from .models import Booking

class UpdateBookingForm(forms.ModelForm):
    """
    Method contains update booking form.
    """
    start_date = forms.DateField(
        widget=forms.DateInput(attrs=dict(type='datetime-local')))
    end_date = forms.DateField(
        widget=forms.DateInput(attrs=dict(type='datetime-local')))

    class Meta:
        """
        Form options.
        """
        model = Booking
        fields = ['address', 'city', 'county', 'start_date', 'end_date']

    def __init__(self, *args, **kwargs):
        """
        Intialise update booking form.
        """
        super(UpdateBookingForm, self).__init__(*args, **kwargs)
        self.fields['address'].widget.attrs.update(
            {"class": "form-control mb-3"})
        self.fields['city'].widget.attrs.update({"class": "form-control mb-3"})
        self.fields['county'].widget.attrs.update(
            {"class": "form-control mb-3"})
        self.fields['start_date'].widget.attrs.update(
            {"class": "form-control mb-3"})
        self.fields['end_date'].widget.attrs.update(
            {"class": "form-control mb-3"})


class CreateBookingForm(forms.ModelForm):
    """
    This class contains create/add booking form.
    """
    start_date = forms.DateTimeField(
        widget=forms.DateInput(attrs={'type': 'datetime-local'}))
    end_date = forms.DateTimeField(
        widget=forms.DateInput(attrs={'type': 'datetime-local'}))

    class Meta:
        """
        Form options.
        """
        model = Booking
        fields = ['address', 'city', 'county', 'start_date',
                  'end_date', 'pickup_location', 'dropoff_location']

    def __init__(self, *args, **kwargs):
        """
        Initialise create booking form.
        """
        super(CreateBookingForm, self).__init__(*args, **kwargs)
        self.fields['address'].widget.attrs.update(
            {"class": "form-control mb-3"})
        self.fields['city'].widget.attrs.update({"class": "form-control mb-3"})
        self.fields['county'].widget.attrs.update(
            {"class": "form-control mb-3"})
        self.fields['start_date'].widget.attrs.update(
            {"class": "form-control mb-3"})
        self.fields['end_date'].widget.attrs.update(
            {"class": "form-control mb-3"})
        self.fields['pickup_location'].widget.attrs.update(
            {"class": "form-control mb-3"})
        self.fields['dropoff_location'].widget.attrs.update(
            {"class": "form-control mb-3"})

        self.fields['pickup_location'].disabled = True
        self.fields['dropoff_location'].disabled = True
