from django import forms
from .models import Product, ProductVariant

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price']

class ProductVariantForm(forms.ModelForm):
    class Meta:
        model = ProductVariant
        fields = ['product', 'color', 'size', 'additional_price']
