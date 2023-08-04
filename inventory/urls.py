from django.urls import path

#import the views from views.py
from .views import upload_product,product_detail,products_list
from .import views

urlpatterns = [
    path("products/upload", upload_product, name="product_upload_view"),
    path("products/list", products_list, name = "products_list_view"),
    path("products/<int:id>/",product_detail, name="product_detail_view"),
    # path("")
    path("",views.index, name='indexx'),
    path('cart/', views.cart , name='cartt'),
    
]

#from the above you have the path   and the view should go to the upload_product from the views.py and now the path name 95432=