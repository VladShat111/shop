from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="carts")
    total_sum = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)

    def __str__(self):
        return str(self.id)


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name="items")
    cart = models.ForeignKey(Cart, on_delete=models.SET_NULL, null=True, related_name="items")
    amount = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    
    @property
    def calc_total_price(self):
        return self.product.price

    def __str__(self):
        return 'Cart item for product {}'.format(self.product.name)
