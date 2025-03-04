from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.CharField(max_length=2000)
    image_url = models.CharField(max_length=256)
    owner = models.ForeignKey(User, default=None, blank=True, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.name