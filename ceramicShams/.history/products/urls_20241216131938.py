from django.urls import path
from . import views

urlpatterns = [
    path('', views.productsList),
    path('<slug:slug>', views.productDetails, name='productDetails')
]
