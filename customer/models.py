from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(null=True)
    address = models.CharField()
    verified_at = models.DateTimeField(null=True)
