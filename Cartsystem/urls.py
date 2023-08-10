from django.urls import path
from .views import upload_cart
urlpatterns = [
    path("cart/upload",upload_cart,name="cart_upload_view"),
        # path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),

]