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


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    amount = models.PositiveIntegerField(default=1)
    item_total = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)

    def __str__(self):
        return f'Cart item for product {self.product.name}'


class Cart(models.Model):
    items = models.ManyToManyField(CartItem, blank=True)
    cart_total = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)

    def __str__(self):
        return str(self.id)
