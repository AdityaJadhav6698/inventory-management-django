from django.db import models

from django.db import models

class ChemicalProduct(models.Model):
    name = models.CharField(max_length=100)
    cas_number = models.CharField(max_length=50, unique=True)
    unit = models.CharField(
        max_length=10,
        choices=[('KG', 'KG'), ('MT', 'MT'), ('Litre', 'Litre')]
    )

    def __str__(self):
        return self.name


class Inventory(models.Model):
    product = models.OneToOneField(ChemicalProduct, on_delete=models.CASCADE)
    quantity = models.FloatField(default=0)

    def __str__(self):
        return f"{self.product.name} - {self.quantity}"



