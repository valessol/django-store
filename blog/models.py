from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from datetime import date

class BlogEntry(models.Model):
    title = models.CharField(max_length=50, verbose_name='Título')
    description = RichTextField(verbose_name='Descripción')
    image = models.ImageField(verbose_name='Imagen')
    outstanding = models.BooleanField(default=False, verbose_name='Destacar')
    review = models.CharField(max_length=50)
    category = models.CharField(max_length=50, verbose_name='Categoría')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField(default=date.today)

class Comment(models.Model):
    comment = models.TextField()
    entry_id = models.ForeignKey(BlogEntry, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField(default=date.today)
