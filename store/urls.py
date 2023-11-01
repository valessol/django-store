from django.urls import path
from store.views import initialize, products, add_item, add_to_cart, contact

urlpatterns = [
    path('', initialize, name='inicio'),
    path('productos', products, name='productos'),
    path('productos/agregar', add_item, name='agregar_producto'),
    path('carrito/agregar', add_to_cart, name='agregar_al_carrito'),
    path('contacto', contact, name='contacto')
]