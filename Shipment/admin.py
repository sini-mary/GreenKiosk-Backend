from django.contrib import admin

# Register your models here.
from .models import Shipment
class ShipmentAdmin(admin.ModelAdmin):
    list_display =('date','order','location','type_of_delivery','status')
admin.site.register(Shipment,ShipmentAdmin)
