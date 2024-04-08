from django import forms
from .models import Product, Supplier

class ProductForm(forms.ModelForm):
    class Meta:
        model1 = Product
        fields = ['name', 'price', 'stock_quantity', 'supplier']

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['name','contact_person','email', 'phone_number']