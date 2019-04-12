from django.urls import path
from .views import ProductView, register, calculate, ProductDetail
from django.contrib.auth import views
urlpatterns = [
    path('products/', ProductView.as_view(), name='products'),
    path('calculate/', calculate, name='calculate'),
    path('product-detail/<str:name>/<int:pk>/', ProductDetail.as_view(), name='product_detail'),
    path('register/', register, name='register'),
    path('login/', views.LoginView.as_view(template_name='apps/products/user/login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(template_name='apps/products/user/logout.html'), name='logout'),
]
