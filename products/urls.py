from django.urls import path
from .views import ProductsListView,register
from django.contrib.auth import views
urlpatterns = [
    path('products/', ProductsListView.as_view(), name='products'),
    path('register/', register, name='register'),
    path('login/', views.LoginView.as_view(template_name='apps/products/user/login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(template_name='apps/products/user/logout.html'), name='logout'),
]
