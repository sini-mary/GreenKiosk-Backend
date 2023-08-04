from django import forms
from .models import  Cart

class CartuploadForm(forms.ModelForm):
    class Meta: 
        model = Cart
        fields = '__all__'