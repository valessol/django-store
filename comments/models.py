from datetime import date
from django.db import models

from blog.models import BlogEntry
from users.models import UserData

class Comment(models.Model):
    blogentry = models.ForeignKey(BlogEntry, on_delete=models.CASCADE)
    userdata = models.ForeignKey(UserData, on_delete=models.CASCADE)
    related_to = models.IntegerField(default=0)
    comment = models.TextField()
    created_at = models.DateField(default=date.today)

