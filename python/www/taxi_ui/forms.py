__author__ = 'pylover'
from django import forms
from django.forms.models import ModelChoiceField
from django.forms import ChoiceField

from taxi_trip.models import Trip, VehicleOptions
from taxi_customer.models import Customer

from smart_selects.form_fields import ChainedModelChoiceField


class TripForm(forms.ModelForm):
    """

    """
    pickup_point = forms.CharField(max_length=300)
    destination_point = forms.CharField(max_length=300)
    landmark = forms.CharField(max_length=300)
    vehicle_options = ChainedModelChoiceField(app_name="taxi_trip",
                      model_name="VehicleOptions",
                      chain_field='vehicle_options', model_field="option_name",
                      auto_choose=True, custom_message="Entry Your Own Choice:", empty_label='____select____',
                      )

    class Meta:
        model = Trip
        exclude = ('ip', 'tokens', 'interest')


class CustomerSigninForm(forms.ModelForm):
    """
    """
    user_name = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Customer
        exclude = ('first_name', 'last_name', 'mobile', 'mobile', 'address', 'language', 'timezone', 'currency', 'language',
                   'currency', 'dob', 'registered_at', 'is_verified', 'verified_at', 'is_active',
                   'active_at', 'gender', 'home_pickup_location', 'destination_pickup', 'social_points',
                   'earned_social_points', 'loyalty_points', 'earned_loyalty_points', 'level',
                   'account_creation_ip', 'email_notify', 'logged_in', 'can_chat')

class ForgotPasswordForm(forms.ModelForm):
    """
    """
    user_name = forms.CharField()

    class Meta:
        model = Customer
        exclude = ('password', 'first_name', 'last_name', 'mobile', 'mobile', 'address', 'language', 'timezone', 'currency', 'language',
                   'currency', 'dob', 'registered_at', 'is_verified', 'verified_at', 'is_active',
                   'active_at', 'gender', 'home_pickup_location', 'destination_pickup', 'social_points',
                   'earned_social_points', 'loyalty_points', 'earned_loyalty_points', 'level',
                   'account_creation_ip', 'email_notify', 'logged_in', 'can_chat')


class CustomerSignupForm(forms.ModelForm):
    """
    """
    email = forms.EmailField(required=False)
    mobile = forms.CharField(required=False)

    def clean(self):
        if not self.data['email'] and not self.data['mobile']:
            raise forms.ValidationError("Please fill one field.")
        return self.cleaned_data

    class Meta:
        model = Customer
        exclude = ('first_name', 'last_name', 'user_name', 'address', 'language', 'timezone', 'currency', 'language',
                   'currency', 'dob', 'registered_at', 'is_verified', 'verified_at', 'is_active',
                   'active_at', 'gender', 'home_pickup_location', 'destination_pickup', 'social_points',
                   'earned_social_points', 'loyalty_points', 'earned_loyalty_points', 'level',
                   'account_creation_ip', 'email_notify', 'logged_in', 'can_chat', 'password')

