from django.contrib import admin

from .models import Trip, CustomerInterest, VehicleOptions
from .forms import TripAdminForm


class TripAdmin(admin.ModelAdmin):
    """"""
    form = TripAdminForm
    list_display = ('customers', 'pickup_point', 'destination_point', 'timestamp', 'landmark', 'email', 'mobile', 'details')

    def customers(self, obj):
        """"""
        return obj.customer

    def details(self, obj):
        """"""
        return u'<a href="/admin/taxi_trip/trip/%d">See Details</a>' % (obj.id,)

    details.allow_tags = True
    details.short_description = "See Details"
    list_editable = ('landmark',)

    class Media:
        js = ("/static/js/admin/jquery-1.10.2.min.js", 
             "https://maps.googleapis.com/maps/api/js?v=3.exp&sensor=false&libraries=places",
             "/static/js/admin/google_api.js")

    def save_model(self, request, obj, form, change):
        ''' '''
        obj.ip = request.META['REMOTE_ADDR']
        obj.save()

    def __init__(self, *args, **kwargs):
        super(TripAdmin, self).__init__(*args, **kwargs)
        self.list_display_links = (None, )

admin.site.register(Trip, TripAdmin)
admin.site.register(VehicleOptions)


