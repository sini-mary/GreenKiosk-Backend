# from .import views
from .views  import customer_create_view,customer_list,customer_detail
from.views import edit_customer
from django.urls import path


urlpatterns = [
   path("Customer/create/",customer_create_view, name= "create_customer"),
   path("Customer/list/", customer_list, name = "customer_list_view"),
   path("Customer/<int:id>/",customer_detail, name="customer_detail_view"),
   path("Customer/edit/<int:id>/", edit_customer, name="customer_edit_view"),

]
