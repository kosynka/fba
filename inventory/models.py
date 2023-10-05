from django.db import models

class Status(models.IntegerChoices):
    NO_DATA = 0, 'no data'
    IN_STOCK = 1, 'in stock'
    OUT_OF_STOCK = 2, 'out of stock'

class Inventory(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(null=True)
    quantity = models.IntegerField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    last_stocked_date = models.DateTimeField()
    status = models.SmallIntegerField(default=0, choices=Status.choices)
