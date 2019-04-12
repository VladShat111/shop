from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Product
from cart.models import CartItem
from django.views.generic import ListView, DetailView
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class ProductView(ListView):
    model = Product
    template_name = 'apps/products/products.html'
    context_object_name = 'product'


class ProductDetail(DetailView):
    model = Product
    template_name = 'apps/products/product_detail.html'


def calculate(request):
    '''
    if request.method == 'POST':
        weight = request.POST.get('userWeight')
        protein = float(weight) * 1.5
        carbohydrates = weight * 4
        fat = float(weight) * 1.2
        calories = (protein + carbohydrates) * 4 + (fat * 9)
        context = {
            'protein': protein,
            'carbohydrates': carbohydrates,
            'fat': fat,
            'calories': calories
        }
    context = context
    '''
    return render(request, 'apps/products/calculation.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, 
                '{}, your account has been created. Now you are able to log in'.format(username)
            )
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'apps/products/user/register.html', {'form': form})

