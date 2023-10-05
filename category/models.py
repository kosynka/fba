from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1000, null=True)
    parent = models.ForeignKey('self', related_name='parent_id', default=0, on_delete=models.SET_DEFAULT, null=True, blank=True)
