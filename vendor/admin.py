from django.contrib import admin

# Register your models here.
from .models import Vendor
class VendorAdmin(admin.ModelAdmin):
    list_display= ('vendor_name','location','contact','store_name','password','username')
admin.site.register(Vendor,VendorAdmin)






