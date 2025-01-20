from django.shortcuts import render
from .models import Product
# Create your views here.


def productsList(request):
    products = Product.objects.all()
    ret render(request, 'products/productsList.html', {
        'products': products
    })
