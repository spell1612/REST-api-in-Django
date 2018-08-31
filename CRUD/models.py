from django.db import models

# Create your models here.
class RandObject(models.Model):
    objectname=models.CharField(max_length=140)
    date_added=models.DateTimeField('Date Published')
    price=models.IntegerField(default=0)
