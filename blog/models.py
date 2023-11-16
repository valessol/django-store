from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from datetime import date
from users.models import UserData

class BlogEntry(models.Model):
    userdata = models.ForeignKey(UserData, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, verbose_name='Título')
    description = RichTextField(verbose_name='Descripción')
    image = models.ImageField(verbose_name='Imagen', upload_to='entries', null=True, blank=True, default='')
    outstanding = models.BooleanField(default=False, verbose_name='Destacar')
    review = models.CharField(max_length=50, default='')
    category = models.CharField(max_length=50, verbose_name='Categoría')
    created_at = models.DateField(default=date.today)
