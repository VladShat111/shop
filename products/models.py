from django.db import models
from django.urls import reverse
# Create your models here.


class ProductManager(models.Manager):
    def all(self, *args, **kwargs):
        return super(ProductManager, self).get_queryset().filter(available=True)


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    stock = models.IntegerField()
    description = models.TextField(null=True)
    img = models.ImageField(upload_to='images_products', null=True, blank=True)
    pub_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    available = models.BooleanField(default=True)
    object = ProductManager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'name': self.name, 'pk': self.pk})
