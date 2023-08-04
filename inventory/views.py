from django.shortcuts import render
from .forms import ProductuploadForm
from inventory.models import Product

#there are class based views and function based views
# Create your views here.
def upload_product(request):                      #the request represents a http request
    if request.method == 'POST':
        uploaded_product = request.FILES["image"]
        form = ProductuploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = ProductuploadForm()
        
    return render(request, "inventory/product_upload.html", {"form": form})
  
  
  #returns many products 
def products_list(request):
    products = Product.objects.all()
    return render (request, "inventory/products_list.html", {"products": products})
  
  #return a single product 
def  product_detail(request,id):
  product = Product.objects.get(id =id)
  return render(request,"inventory/product_detail.html",{"product":product})



def index(request):
  return render(request,"inventory/index.html")


def cart(request):
  return render(request,"inventory/cart.html")


def cart_upload(request):
  return render(request,"cart/cart_upload.html")










