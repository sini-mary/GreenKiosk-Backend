from .views import vendor_create_view,vendor_list
from django.urls import path

urlpatterns = [
    path("vendor/create/",vendor_create_view,name="create_vendor"),
    path("vendor/list/",vendor_list,name="vendor_list_view")
]
