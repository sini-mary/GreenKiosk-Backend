from django.urls import path
from.views import CustomerListView,CustomerDetailView,CartListAPIView,CartDetailAPIView
from.views import  ProductListView,ProductDetailView,OrderDetailView,OrderListView


urlpatterns = [
    path("customers/list",CustomerListView.as_view(),name="customer_list_view" ),
    path("customers/<int:id>/",CustomerDetailView.as_view(),name="customer_detail_view"),
     path('Cart/list',CartListAPIView.as_view(), name='cart-list'),
    path('Cart/<int:pk>/', CartDetailAPIView.as_view(), name='cart-detail'),
    path('Cart/<int:pk>/add_product/', CartDetailAPIView.as_view(),
         name='cart-add-product'),
    path('products/list', ProductListView.as_view(), name='product-list'),
    path('products/<int:id>/', ProductDetailView.as_view(), name='product-detail'),
    path('orders/list', OrderListView.as_view(), name='order-list'),
    path('orders/<int:id>/', OrderDetailView.as_view(), name='order-detail'),  # This pattern is for retrieving a single order
]  
    

