from django import forms
from .models import Product


class ProductuploadForm(forms.ModelForm):
    class Meta :
       model = Product                    # model to create our form for products
       fields = "__all__"