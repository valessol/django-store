from django.db import models
from django.contrib.auth.models import User

class UserData(models.Model): 
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=50)
    entries = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)
    biography = models.CharField(max_length=300, default='')
    avatar = models.ImageField(upload_to='avatars', null=True, blank=True, default='')