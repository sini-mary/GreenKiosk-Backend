from django.shortcuts import render,redirect
from .forms import CustomerDetailsForm
from Customer.models import Customer


def customer_create_view(request):
    if request.method == "POST":
        form = CustomerDetailsForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CustomerDetailsForm()
    
    return render(request, "Customer/customer_form.html", {'form': form})


def customer_list(request):
    customer = Customer.objects.all()
    return render (request, "Customer/customer_list.html", {"customer": customer})


def edit_customer(request,id):
    customer= Customer.objects.get(id=id)
    
    if request.method =='POST':
        form = CustomerDetailsForm(request.POST,instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer_detail_view',id=id)
        
        else:
            form =CustomerDetailsForm(instance=customer)
            return redirect(request,'Customer/customer_edit.html',{'form':form})
        
        
def  customer_detail(request,id):
  customer = Customer.objects.get(id =id)
  return render(request,'Customer/customer_detail.html',{"customer":customer})
