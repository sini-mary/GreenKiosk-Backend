from django.contrib import admin

# Register your models here.
from .models import Notification
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('message','time','customer')
admin.site.register(Notification,NotificationAdmin)
