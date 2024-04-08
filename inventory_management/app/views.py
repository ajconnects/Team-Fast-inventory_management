from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Product, Supplier
from .forms import ProductForm, SupplierForm  # Assuming create forms for input
from django.http import HttpResponse


def home(request):
    return HttpResponse("Welcome to Team Fast Django Inventory Management System")

# CRUD operations  (Create, Read, Update and Delete) 

#   Create Operations
    
def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')  # Redirect to product list page
    else:
        form = ProductForm()
    return render(request, 'create_product.html', {'form': form})


def create_supplier(request):
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('supplier_list')  # Redirect to supplier list page
    else:
        form = SupplierForm()
    return render(request, 'create_supplier.html', {'form': form})

# Read Operation
def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})


def supplier_list(request):
    suppliers = Supplier.objects.all()
    return render(request, 'supplier_list.html', {'suppliers': suppliers})

#   Update Operations
def update_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')  # Redirect to product list page
    else:
        form = ProductForm(instance=product)
    return render(request, 'update_product.html', {'form': form})


def update_supplier(request, supplier_id):
    supplier = get_object_or_404(Supplier, pk=supplier_id)
    if request.method == 'POST':
        form = SupplierForm(request.POST, instance=supplier)
        if form.is_valid():
            form.save()
            return redirect('supplier_list')  # Redirect to supplier list page
    else:
        form = SupplierForm(instance=supplier)
    return render(request, 'update_supplier.html', {'form': form})

#   Delete Operations
def delete_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')  # Redirect to product list page
    return render(request, 'confirm_delete_product.html', {'product': product})


def delete_supplier(request, supplier_id):
    supplier = get_object_or_404(Supplier, pk=supplier_id)
    if request.method == 'POST':
        supplier.delete()
        return redirect('supplier_list')  # Redirect to supplier list page
    return render(request, 'confirm_delete_supplier.html', {'supplier': supplier})


