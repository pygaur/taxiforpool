__author__ = 'pylover'
from django import forms

from .models import  EmailTrigger


class EmailTriggerForm(forms.ModelForm):
    ''' '''
    class Meta:
        model = EmailTrigger

