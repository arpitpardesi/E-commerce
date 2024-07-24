from django.contrib import admin
from cars.models import Car

# Register your models here.

# admin.site.register(Car)

class CarAdmin(admin.ModelAdmin):
    fieldsets =  [
        (           'Time Information', {'fields':['year']}),
        ("Car Information", {'fields':['brand']})
    ]
    # fields = ['year','brand']


admin.site.register(Car, CarAdmin)