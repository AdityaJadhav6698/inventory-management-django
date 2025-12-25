from django.contrib import admin
from .models import ChemicalProduct, Inventory

admin.site.register(ChemicalProduct)
admin.site.register(Inventory)
