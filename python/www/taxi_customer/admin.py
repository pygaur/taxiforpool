from django.contrib import admin

# Register your models here.
from .models import Customer, CustomerLevel

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('email', 'mobile', 'user_name')



class CustomerLevelAdmin(admin.ModelAdmin):
    pass

admin.site.register(Customer, CustomerAdmin)
admin.site.register(CustomerLevel, CustomerLevelAdmin)
