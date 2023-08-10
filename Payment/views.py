from django.shortcuts import render
from .forms import PaymentForm

# Create your views here.
def payment_view(request):
    if request.method == 'POST':
        form= PaymentForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            form=PaymentForm()
            return render (request, "payment/payment_form.html",{"form":form})