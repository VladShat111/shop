from django.db import models

# Create your models here.
from django.utils.timezone import now


class Product(models.Model):
    name = models.CharField(max_length=60)
    price = models.FloatField()
    stock = models.IntegerField()
    img = models.ImageField(upload_to='images_products', null=True, blank=True)
    pub_prod = models.DateTimeField(default=now)
