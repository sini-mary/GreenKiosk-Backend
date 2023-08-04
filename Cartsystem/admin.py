from django.contrib import admin

# Register your models here.
from .models import Cart
class CartAdmin(admin.ModelAdmin):
    list_display = ('product','total','number_of_products','shipping_cost','Payment_options','discounts')
admin.site.register(Cart, CartAdmin)
