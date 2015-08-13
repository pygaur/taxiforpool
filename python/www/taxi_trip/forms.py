__author__ = 'pylover'
from django import forms

from .models import  Trip


class TripAdminForm(forms.ModelForm):
    """

    """
    class Meta:
        model = Trip
        exclude = ('ip', 'tokens')


