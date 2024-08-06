from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, ProductVariant
from .forms import ProductForm, ProductVariantForm

# Product Views
def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products/product_detail.html', {'product': product})

def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'products/product_form.html', {'form': form})

def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'products/product_form.html', {'form': form})

def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'products/product_confirm_delete.html', {'product': product})

# ProductVariant Views
def product_variant_list(request):
    variants = ProductVariant.objects.all()
    return render(request, 'products/product_variant_list.html', {'variants': variants})

def product_variant_detail(request, pk):
    variant = get_object_or_404(ProductVariant, pk=pk)
    return render(request, 'products/product_variant_detail.html', {'variant': variant})

def product_variant_create(request):
    if request.method == 'POST':
        form = ProductVariantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_variant_list')
    else:
        form = ProductVariantForm()
    return render(request, 'products/product_variant_form.html', {'form': form})

def product_variant_update(request, pk):
    variant = get_object_or_404(ProductVariant, pk=pk)
    if request.method == 'POST':
        form = ProductVariantForm(request.POST, instance=variant)
        if form.is_valid():
            form.save()
            return redirect('product_variant_list')
    else:
        form = ProductVariantForm(instance=variant)
    return render(request, 'products/product_variant_form.html', {'form': form})

def product_variant_delete(request, pk):
    variant = get_object_or_404(ProductVariant, pk=pk)
    if request.method == 'POST':
        variant.delete()
        return redirect('product_variant_list')
    return render(request, 'products/product_variant_confirm_delete.html', {'variant': variant})
