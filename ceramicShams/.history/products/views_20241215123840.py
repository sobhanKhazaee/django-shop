from django.shortcuts import render
from .models import Product
# Create your views here.

def productsList(request):
    products = Product.objects
    render(request,'')