from django.contrib import admin

# Register your models here.
from .models import Cart,CartItem
class CartAdmin(admin.ModelAdmin):
    list_display = ('products','total','image')
admin.site.register(Cart, CartAdmin)

class CartItemAdmin(admin.ModelAdmin):
    list_display=('cart', 'product' ,'quantity')
admin.site.register(CartItem,CartItemAdmin)