from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.db.models import Avg

# Create your views here.

class productsListV

def productsList(request):

    products = Product.objects.all()
    # cats = Category.objects.all()
    productsNumber = products.count()
    allProductsRate = products.aggregate(Avg("rate"))
    return render(request, 'products/productsList.html', {
        'products': products,
        'productsNumber': productsNumber,
        'allProductsRate': allProductsRate,
        # 'cats': cats,
    })


def productDetails(request, slug):
    all_cats = Category.objects.all()
    product = get_object_or_404(Product, slug=slug)
    product_tags = product.product_tag.all()
    return render(request, 'products/productDetails.html', {
        'product': product,
        'cats': all_cats,
        'product_tags': product_tags
    })


def sortByCat(request, cat_id):
    all_cats = Category.objects.all()
    cat = Category.objects.get(id=cat_id)
    products = cat.products.all()
    return render(request, 'products/sortedByCat.html', {
        'products': products,
        'cats': all_cats,
        'cat': cat
    })


def sortByTag(request, tag):
    products = Product.objects.filter(product_tag__tag=tag, is_active=True)
    return render(request, 'products/sortByTag.html', {
        'products': products,
    })
