from django.shortcuts import render
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


class UpdateCartItemView(LoginRequiredMixin, UpdateView):
    model = CartItem
    fields = ['product', 'amount', 'total_price']
    template_name = 'apps/cart/cart_item.html'


class DeleteCartItemView(LoginRequiredMixin, DeleteView):
    model = CartItem
    template_name = 'apps/cart/cart_item.html'
    success_url = 'products'
