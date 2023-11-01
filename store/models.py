from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    price = models.IntegerField()
    stock = models.IntegerField()
    image = models.TextField()
    
class Cart(models.Model):
    client = models.CharField(max_length=30)
    product = models.CharField(max_length=50)
    quantity = models.IntegerField()

class Query(models.Model):
    nombre_de_contacto = models.CharField(max_length=30)
    consulta = models.CharField(max_length=255)
    telefono = models.IntegerField()
