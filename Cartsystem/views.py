from django.shortcuts import render
from .forms import CartuploadForm

# Create your views here.
def upload_cart(request):
    form = CartuploadForm()
    return render(request,"cart/cart_upload.html",{"form":form})
