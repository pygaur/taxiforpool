from django.db import models

class CustomerLevel(models.Model):
    """ """
    name = models.CharField(max_length=10)

    def __unicode__(self):
        return self.name
    
class Customer(models.Model):
    """ """
    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    user_name = models.CharField(max_length=30)
    password = models.CharField(max_length=128)
    address = models.TextField(null=True, blank=True)
    timezone = models.CharField(max_length=30, null=True, blank=True)
    language = models.CharField(max_length=10, null=True, blank=True)
    currency = models.CharField(max_length=5, null=True, blank=True)
    dob = models.DateTimeField(null=True, blank=True)
    registered_at = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(null=True, blank=True)
    mobile = models.CharField(max_length=20, null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    verified_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)
    active_at = models.DateTimeField(auto_now_add=True)
    gender = models.CharField(max_length=20)
    home_pickup_location = models.CharField(max_length=300)
    destination_pickup = models.CharField(max_length=300)
    social_points = models.DecimalField(max_digits=10, decimal_places=2,
                                        default=0.00)	
    earned_social_points  = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)	
    loyalty_points  = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)	
    earned_loyalty_points = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)	
    level = models.ForeignKey('CustomerLevel')	
    account_creation_ip = models.IPAddressField()	
    email_notify = models.BooleanField(default=True)	
    logged_in = models.BooleanField(default=False)	
    can_chat = models.BooleanField(default=True)	
#    affiliate = models.ForeignKey(Affiliate)
#    campaign = models.ForeignKey(Campaign)

    def __unicode__(self):
        return self.id


class Activity(models.Model):
    """"""
    activity_name = models.CharField(max_length=30)
    last_updated = models.DateTimeField(auto_now=True)


class ActivityLogs(models.Model):
    """"""
    activity_name = models.ForeignKey("Activity")
    timestamp = models.DateTimeField(auto_now_add=True)
    ip = models.IPAddressField()



