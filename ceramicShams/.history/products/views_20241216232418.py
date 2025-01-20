from django.shortcuts import render, get_object_or_404
from .models import Product
from django.db.models import Avg

# Create your views here.


def productsList(request):
    products = Product.objects.all()
    productsNumber = products.count()
    allProductsRate = products.aggregate(Avg("rate"))
    return render(request, 'products/productsList.html', {
        'products': products,
        'productsNumber': productsNumber,
        'allProductsRate': allProductsRate,
    })


def productDetails(request, slug):
    # product = Product.objects.filter(id=product_id)
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'products/productDetails.html', {
        'product': product
    })
$product = 
