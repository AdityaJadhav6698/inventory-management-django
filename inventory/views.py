from django.shortcuts import render, redirect
from .models import ChemicalProduct, Inventory


def inventory_list(request):
    inventory = Inventory.objects.select_related('product')
    return render(request, 'inventory_list.html', {'inventory': inventory})


def add_product(request):
    error = None

    if request.method == 'POST':
        name = request.POST['name']
        cas = request.POST['cas']
        unit = request.POST['unit']

        # ✅ CHECK FOR DUPLICATE CAS NUMBER
        if ChemicalProduct.objects.filter(cas_number=cas).exists():
            error = "Product with this CAS number already exists."
        else:
            product = ChemicalProduct.objects.create(
                name=name,
                cas_number=cas,
                unit=unit
            )
            Inventory.objects.create(product=product)
            return redirect('inventory_list')

    return render(request, 'add_product.html', {'error': error})


def update_stock(request, product_id):
    inventory = Inventory.objects.get(product_id=product_id)

    if request.method == 'POST':
        qty = float(request.POST['quantity'])
        action = request.POST['action']

        if qty > 0:
            if action == 'IN':
                inventory.quantity += qty
            elif action == 'OUT' and qty <= inventory.quantity:
                inventory.quantity -= qty

            inventory.save()

    return redirect('inventory_list')

