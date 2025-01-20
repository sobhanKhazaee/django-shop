from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.db.models import Avg

# Create your views here.


def productsList(request,cat_id):
    if cat_id is None
    products = Product.objects.all()
    cats = Category.objects.all()
    productsNumber = products.count()
    allProductsRate = products.aggregate(Avg("rate"))
    return render(request, 'products/productsList.html', {
        'products': products,
        'productsNumber': productsNumber,
        'allProductsRate': allProductsRate,
        'cats':cats,
    })


def productDetails(request, slug):
    # product = Product.objects.filter(id=product_id)
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'products/productDetails.html', {
        'product': product
    })


def sortByCat(request, cat_id):
    cat = Category.objects.get(id=cat_id)
    product = cat.products.all()
    return render(request, 'products/productsList.html', {
        'product': product,
    })
