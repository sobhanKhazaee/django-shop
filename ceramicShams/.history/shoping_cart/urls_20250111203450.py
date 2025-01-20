from django.urls import path
from . import views

urlpatterns = [
   path('add-to-cart/', views.add_to_cart, name='add_to_cart'),
   path('cart-page/',views.CartView,name="cart_page"),
   path('removefrom_cart/',views.remove_from_cart,name="remove_from_cart"),
   
]