from django.db import models
from ckeditor.fields import RichTextField

class BlogEntry(models.Model):
    title = models.CharField(max_length=50)
    description = RichTextField()
    image = models.ImageField()
    user_id = models.CharField(max_length=50)
    created_at = models.DateField()

class Comment(models.Model):
    comment = models.TextField()
    entry_id = models.CharField(max_length=50)
    user_id = models.CharField(max_length=50)
    created_at = models.DateField()
