from django.urls import path
from main.views import initialize, products

urlpatterns = [
    path('', initialize, name='inicio'),
    path('productos', products, name='productos')
]