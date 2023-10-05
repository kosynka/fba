from django.db import models
from customer.models import Customer

class Status(models.IntegerChoices):
    NO_DATA = 0, 'no data'
    CREATED = 0, 'created'
    PENDING = 1, 'pending'
    PROCESSING = 2, 'processing'
    SHIPPED = 2, 'shipped'
    Delivered = 2, 'delivered'
    CANCELED = 2, 'canceled'
    REFUNDED = 2, 'refunded'

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateTimeField()
    total_price = models.FloatField()
    status = models.SmallIntegerField(default=0, choices=Status.choices)
