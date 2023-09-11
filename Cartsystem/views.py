from django.shortcuts import render,redirect
from .forms import CartuploadForm
from Cartsystem.models import Cart,CartItem
from inventory.models import Product
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
@login_required
# def upload_cart(request):                      #the request represents a http request
#     if request.method == 'POST':
#         uploaded_product = request.FILES["image"]
#         form = CartuploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#     else:
#         form = CartuploadForm()
        
#     return render(request, "cart/cart_list.html", {"form": form})

  
# def cart_list(request):
#      cart= Cart.objects.all()
#      return render (request,"cart/cart_list.html",{"cart":cart})        
 
# def  cart_detail(request,id):
#   product = Product.objects.get(id =id)
#   return render(request,"cart/cart_detail_view.html",{"product":product})

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart/cart_list.html') 

def cart_list(request):
    cart = Cart.objects.filter(user=request.user).first()
    if cart:
        cart_items = cart.cartitem_set.all()
    else:
        cart_items = []
    return render(request, 'cart/cart_list.html', {'cart_items': cart_items})
