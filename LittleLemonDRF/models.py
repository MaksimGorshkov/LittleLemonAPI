from typing import Type

from django.db import models
from django.db.models import IntegerField


class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    inventory = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    def __str__(self):
        return self.title
