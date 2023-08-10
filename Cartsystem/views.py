from django.shortcuts import render
from .forms import CartuploadForm
def upload_cart(request):
    form = CartuploadForm()
    return render(request,"cart/cart_upload.html",{"form":form})

# def view_cart(request):
#     cart = get_object_or_404(Cart, user=request.user)
#     cart_items = cart.items.all()
#     total_price = sum(item.product.price * item.quantity for item in cart_items)
    
#     return render(request, 'cart/cart.html', {'cart_items': cart_items, 'total_price': total_price})