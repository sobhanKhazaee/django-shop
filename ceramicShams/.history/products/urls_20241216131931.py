from django.urls import path
from . import views

urlpatterns = [
    path('', views.productsList),
    path('<slug:product_id>', views.productDetails, name='productDetails')
]
