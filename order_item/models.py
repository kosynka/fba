from django.db import models
from order.models import Order
from product.models import Product

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='order_id', on_delete=models.SET_NULL, null=True, blank=True)
    product = models.ForeignKey(Product, related_name='product_id', on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField()
    price = models.FloatField()
    subtotal = models.FloatField(default=0, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.subtotal = self.quantity * self.price

        super(Customer, self).save(*args, **kwargs)
