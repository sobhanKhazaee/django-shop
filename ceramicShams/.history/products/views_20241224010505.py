from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.db.models import Avg
from django.views.generic import ListView ,DetailView

# Create your views here.

# لیست  همه ی محصولاتتن
class productsListView(ListView):
    template_name = 'products/productsList.html'
    model = Product
    context_object_name = 'products'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['productsNumber'] = self.get_queryset().count()
        context['allProductsRate'] = self.get_queryset().aggregate(Avg('rate'))[
            'rate__avg']
        return context

# جزئیات محصول
class productDetailsView(DetailView):
    template_name = 'products/productDetails.html'
    model = Product
    context_object_name = "product"


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
