from django.db import models
from customer.models import Customer

class Status(models.IntegerChoices):
    NO_DATA = 0, 'no data'
    CREATED = 1, 'created'
    PENDING = 2, 'pending'
    PROCESSING = 3, 'processing'
    SHIPPED = 4, 'shipped'
    Delivered = 5, 'delivered'
    CANCELED = 6, 'canceled'
    REFUNDED = 7, 'refunded'

class Order(models.Model):
    customer = models.ForeignKey(Customer, related_name='customer_id', on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateTimeField()
    total_price = models.FloatField()
    status = models.SmallIntegerField(default=Status.NO_DATA, choices=Status.choices)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
