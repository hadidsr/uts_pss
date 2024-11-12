from django.shortcuts import render, redirect, get_object_or_404
from .models import *

# Create your views here.
from .forms import *

## Manage Items
# Create Item
def create_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('items')
    else:
        form = ItemForm()
    return render(request, 'items/create_item.html', {'form': form})

# Read Items
def items(request):
    items = Item.objects.all()
    return render(request, 'items/items.html', {'items': items})

# Update Item
def update_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('items')
    else:
        form = ItemForm(instance=item)
    return render(request, 'items/update_item.html', {'form': form, 'item': item})

# Delete Item
def delete_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    if request.method == 'POST':
        item.delete()
        return redirect('items')
    return render(request, 'items/delete_item.html', {'item': item})

## Manage Categories
# Create Category
def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
    else:
        form = CategoryForm()
    return render(request, 'categories/create_category.html', {'form': form})

# Read Categories
def categories(request):
    categories = Category.objects.all()
    return render(request, 'categories/categories.html', {'categories': categories})

# Update Category
def update_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'categories/update_category.html', {'form': form, 'category': category})

# Delete Category
def delete_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    if request.method == 'POST':
        category.delete()
        return redirect('categories')
    return render(request, 'categories/delete_category.html', {'category': category})

## Manage Suppliers
# Create Supplier
def create_supplier(request):
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('suppliers')
    else:
        form = SupplierForm()
    return render(request, 'suppliers/create_supplier.html', {'form': form})

# Read Suppliers
def suppliers(request):
    suppliers = Supplier.objects.all()
    return render(request, 'suppliers/suppliers.html', {'suppliers': suppliers})

# Update Supplier
def update_supplier(request, supplier_id):
    supplier = get_object_or_404(Supplier, pk=supplier_id)
    if request.method == 'POST':
        form = SupplierForm(request.POST, instance=supplier)
        if form.is_valid():
            form.save()
            return redirect('suppliers')
    else:
        form = SupplierForm(instance=supplier)
    return render(request, 'suppliers/update_supplier.html', {'form': form, 'supplier': supplier})

# Delete Supplier
def delete_supplier(request, supplier_id):
    supplier = get_object_or_404(Supplier, pk=supplier_id)
    if request.method == 'POST':
        supplier.delete()
        return redirect('suppliers')
    return render(request, 'suppliers/delete_supplier.html', {'supplier': supplier})