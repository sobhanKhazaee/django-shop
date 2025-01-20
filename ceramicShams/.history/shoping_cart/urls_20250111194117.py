from django.urls import path
from . import views

urlpatterns = [
   path('add-to-cart/', views.add_to_cart, name='add_to_cart'),
   path('cart-page/',views.CartView,)
]