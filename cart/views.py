from django.http import HttpResponse
from django.shortcuts import render

from products.models import Product
from .models import Cart, CartItem
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
# Create your views here.

#Views for cart


class CreateCartView(LoginRequiredMixin, CreateView):
    model = Cart
    fields = ['user', 'total_sum']
    template_name = 'apps/cart/'


class UpdateCartView(LoginRequiredMixin, UpdateView):
    model = Cart
    fields = ['user']
    template_name = 'apps/cart/cart.html'


class DeleteCartView(LoginRequiredMixin, DeleteView):
    model = Cart
    template_name = 'apps/cart/cart.html'
    success_url = 'product'

#Views for cart items


class CreateCartItemView(LoginRequiredMixin, CreateView):
    model = CartItem
    fields = ['product', 'amount', 'total_price']
    template_name = 'apps/cart/cart_item.html'

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            product_id = request.POST.get('product_id')
            product_name = request.POST.get('product_name')
            product_price = request.POST.get('product_price')
            cart_id = request.POST.get('cart_id')
            product = Product.object.filter(pk=product_id).first()
            cart = Cart.objects.filter(pk=cart_id).first()
            cart_item = CartItem(
                product=product,
                cart=cart,
                total_price=product_price
            )  # TODO: use create_or_update
            cart_item.save()
            cart_item_all = CartItem.objects.all()
            context = {'cart_item': cart_item_all}
            return render(request, 'apps/cart/cart_item.html', context)


class UpdateCartItemView(LoginRequiredMixin, UpdateView):
    model = CartItem
    fields = ['product', 'amount', 'total_price']
    template_name = 'apps/cart/cart_item.html'


class DeleteCartItemView(LoginRequiredMixin, DeleteView):
    model = CartItem
    template_name = 'apps/cart/cart_item.html'
    success_url = ''

