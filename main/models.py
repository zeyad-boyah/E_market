from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    stock = models.IntegerField(default=100)
    description = models.CharField(max_length=2000)
    image_url = models.CharField(max_length=256)

    def __str__(self):
        return self.name
