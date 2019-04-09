from django.contrib import admin
from .models import Product, CartItem, Cart
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'description', 'available')


class CartItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'amount', 'item_total')


admin.site.register(Product, ProductAdmin)
admin.site.register(CartItem, CartItemAdmin)
admin.site.register(Cart)
