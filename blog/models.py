from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class BlogEntry(models.Model):
    title = models.CharField(max_length=50)
    description = RichTextField()
    image = models.ImageField()
    outstanding = models.BooleanField(default=False)
    review = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField()

class Comment(models.Model):
    comment = models.TextField()
    entry_id = models.ForeignKey(BlogEntry, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField()
