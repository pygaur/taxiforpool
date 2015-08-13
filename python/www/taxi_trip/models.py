from django.db import models

from taxi_customer.models import Customer


class VehicleOptions(models.Model):
    """"""
    option_name = models.CharField(max_length=100)

    def __unicode__(self):
        """"""
        return self.option_name

    class Meta:
        """"""
        app_label = "taxi_trip"


class Trip(models.Model):
    """ to store content of each trip  """
    customer = models.ForeignKey(Customer, null=True, blank=True, related_name="creator")
    pickup_point = models.CharField(null=True, blank=True, max_length=300)
    destination_point = models.CharField(null=True, blank=True, max_length=300)
    landmark = models.CharField(null=True, blank=True, max_length=500)
    timestamp = models.DateTimeField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    mobile = models.CharField(max_length=15, null=True, blank=True)
    vehicle_options = models.CharField(max_length=100)
    interest = models.ManyToManyField(Customer, through="CustomerInterest", symmetrical=False, null=True, blank=True)
    tokens = models.CharField(max_length=16, blank=True)
    ip = models.IPAddressField(null=True, blank=True)

    def __unicode__(self):
        """"""
        return self.pickup_point

    def add_relationship(self, entry):
        """"""
        entry, created = CustomerInterest.objects.get_or_create(
            trip=self,
            customer=entry)
        return entry, created

    class Meta:
        """"""
        app_label = "taxi_trip"


class CustomerInterest(models.Model):
    """ if somebody shows interest into trips"""
    trip = models.ForeignKey(Trip, related_name='source')
    customer = models.ForeignKey(Customer, related_name='customer')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """"""
        app_label = "taxi_trip"


class TripLikeLogs(models.Model):
    """"""
    trip = models.ForeignKey(Trip)
    timestamp = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer, null=True)
    like = models.BooleanField(default=True)
