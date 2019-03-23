from django.shortcuts import render, redirect
from .models import Product
from django.views.generic import ListView
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class ProductsListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'apps/products/products.html'
    context_object_name = 'product'



def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            usrname = form.cleaned_data.get('username')
            messages.success(request, f'{usrname}, your account has been created. Now you are able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'apps/products/user/register.html', {'form': form})
