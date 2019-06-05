from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime 

class List(models.Model):
    id_user = models.IntegerField(null=False)
    name = models.CharField(max_length=255, null=False)
    comment = models.CharField(max_length=2048, null=True, default='')
    estimatedDate = models.DateField(null=True, default=datetime.now )


class ListPlace(models.Model):
    id_list = models.ForeignKey(List, on_delete=models.CASCADE, null=False, related_name='places')
    id_place = models.IntegerField(null=False, default=1)

