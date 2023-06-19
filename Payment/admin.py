from django.contrib import admin

# Register your models here.
from .models import Payment
class Paymentadmin(admin.ModelAdmin):
    list_display = ('payment_method','amount','date','receipt')
admin.site.register(Payment,Paymentadmin)
