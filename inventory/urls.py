from django.urls import path
from . import views

urlpatterns = [
    path('', views.inventory_list, name='inventory_list'),
    path('add/', views.add_product, name='add_product'),
    path('update/<int:product_id>/', views.update_stock, name='update_stock'),
]
