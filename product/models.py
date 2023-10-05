from django.db import models

from category.models import Category

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1000, null=True)
    # manufacturer = models.ForeignKey(Manufacturer, related_name='manufacturer_id', on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey(Category, related_name='category_id', on_delete=models.SET_NULL, null=True, blank=True)
    weight = models.FloatField()
    height = models.FloatField()
    width = models.FloatField()
    depth = models.FloatField()
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
