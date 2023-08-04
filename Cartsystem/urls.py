from django.urls import path
from .views import upload_cart

urlpatterns = [
    path("cart/upload",upload_cart,name="cart_upload_view")
]