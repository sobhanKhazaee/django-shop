from django.shortcuts import render , get_object_or_404
from .models import Product
 
# Create your views here.


def productsList(request):
    products = Product.objects.all()
    return render(request, 'products/productsList.html', {
        'products': products
    })


def productDetails(request, slug):
    # product = Product.objects.filter(id=product_id)
    product = get_object_or_404(Product, slug=s)
    return render(request, 'products/productDetails.html', {
        'product': product
    })
