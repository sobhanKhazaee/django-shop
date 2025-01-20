from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.db.models import Avg
from django.views.generic import ListView ,DetailView

# Create your views here.


class productsListView(ListView):
    template_name = 'products/productsList.html'
    model = Product
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.all()

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['productsNumber'] = self.get_queryset().count()
        context['allProductsRate'] = self.get_queryset().aggregate(Avg('rate'))[
            'rate__avg']
        return context


# def productsList(request):

#     products = Product.objects.all()
#     productsNumber = products.count()
#     allProductsRate = products.aggregate(Avg("rate"))
#     return render(request, 'products/productsList.html', {
#         'products': products,
#         'productsNumber': productsNumber,
#         'allProductsRate': allProductsRate,

#     })

class productDetailsView(DetailView):
    


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
