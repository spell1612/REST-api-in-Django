from django.db import models
from datetime import datetime
# Create your models here.
class RandObject(models.Model):
    objectname=models.CharField(max_length=140,blank=False)
    date_added=models.DateTimeField(default=datetime.now)
    price=models.IntegerField(default=0,blank=False)
    def __str__(self):
        return self.objectname
