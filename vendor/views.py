from django.shortcuts import render
from .forms import  VendorUploadForm
from vendor.models import Vendor
# Create your views here.
def vendor_create_view(request):
    if request.method =='POST':
        form= VendorUploadForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            form=VendorUploadForm()
            return render(request,"vendor/vendor_form.html",{"form":form})
def vendor_list(request):
    vendor=Vendor.objects.all()
    return render(request,"vendor/vendor_list.html",{"vendor":vendor})