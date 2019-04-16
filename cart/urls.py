from django.urls import path
from . import views
urlpatterns = [
    path('', views.CreateCartView.as_view(), name='create_cart'),
    path('<int:pk>/update/', views.UpdateView.as_view(), name='update_cart'),
    path('<int:pk>/delete/', views.DeleteCartView.as_view(), name='delete_cart'),
    path('<int:pk>/cart_item/', views.CreateCartItemView.as_view(), name='create_cart_item'),
    path('<int:pk>/update/', views.UpdateCartItemView.as_view(), name='update_cart_item'),
    path('<int:pk>/delete/', views.DeleteCartItemView.as_view(), name='delete_cart_item'),
]
