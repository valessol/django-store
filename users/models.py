from django.db import models

class UserData(models.Model): 
    username = models.CharField(max_length=50)
    entries = models.IntegerField()
    comments = models.IntegerField()
    biography = models.CharField(max_length=300)
    avatar = models.ImageField(upload_to='avatares', null=True, blank=True)

# import uuid

# myUUID = uuid.uuid4()
# print(type(myUUID))
# print(myUUID)
# myUUIDString = str(myUUID)
# print(type(myUUIDString))
# print(myUUIDString)