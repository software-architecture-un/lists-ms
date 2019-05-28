from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime 

class List(models.Model):
    id_user = models.IntegerField(null=False)
    name = models.CharField(max_length=255, null=False)
    comment = models.CharField(max_length=2048, null=True)
    estimatedDate = models.DateField(null=True, default=datetime.now )
    order = models.IntegerField(null=False)


class ListPlace(models.Model):
    id_list = models.ForeignKey(List, on_delete=models.CASCADE, null=False, related_name='places')
    placeLon = models.FloatField(max_length=30, null=False)
    placeLat = models.FloatField(max_length=30, null=False)

