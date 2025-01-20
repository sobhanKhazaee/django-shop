from django.shortcuts import render
from .models import Product
from django.http import get_object_or_404
# Create your views here.


def productsList(request):
    products = Product.objects.all()
    return render(request, 'products/productsList.html', {
        'products': products
    })


def productDetails(request, product_id):
    product = Product.objects.filter(id=product_id)
    get_object_or_404(pro)
    return render(request, 'products/productsList.html', {
        'products': product
    })
