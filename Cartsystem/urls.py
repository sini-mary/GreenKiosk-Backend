from django.urls import path
from .views import cart_list,add_to_cart
urlpatterns = [
    # path("cart/upload",upload_cart,name="cart_upload_view"),
    # path("cart/list",cart_list,name="cart_list_view"),
    # path("cart/detail",cart_detail,name="cart_detail_view"),
    path('cart/add-to-cart/<int:product_id>/', add_to_cart, name='add-to-cart'),
    path('cart/list',cart_list, name='cart-view'),

    

]