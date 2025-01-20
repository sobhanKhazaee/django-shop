from django.urls import path
from . import views
from django.urls import re_path

urlpatterns = [
    path('', views.productsList),
    path('<slug:slug>', views.productDetails, name='productDetails')
]
