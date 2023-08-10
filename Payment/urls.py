from django.urls import path
from .views import payment_view

urlpatterns = [
    path("payment/list",payment_view,name= "payment_view"),
]


