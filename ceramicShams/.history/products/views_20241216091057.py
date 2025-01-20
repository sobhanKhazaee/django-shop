from django.shortcuts import render
from .models import Product
# Create your views here.


def productsList(request):
    products = Product.objects.all()
    return render(request, 'products/productsList.html', {
        'products': products
    })
    
def productDetails(request,product_id):    
    product= Product.ob
