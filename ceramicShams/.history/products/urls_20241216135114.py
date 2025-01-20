from django.urls import path
from . import views
from django.urls import re_path

urlpatterns = [
    path('', views.productsList),
    # i used re_path becaus i want make a custom slug with 
    re_path(r'^(?P<slug>[-\w\u0600-\u06FF]+)/$',
            views.productDetails, name='productDetails'),
]
