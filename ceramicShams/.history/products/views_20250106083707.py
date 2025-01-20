from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.db.models import Avg
from django.views.generic import ListView, DetailView

# Create your views here.

# لیست  همه ی محصولات


class productsListView(ListView):
    template_name = 'products/productsList.html'
    model = Product
    context_object_name = 'products'
    ordering = ['price']
    paginate_by = 12

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = self.object.product_tag.all()
        return context

# محصولات بر اساس دسته بندی


class sortByCatView(ListView):
    template_name = 'products/productsList.html'
    model = Product
    context_object_name = 'products'
    ordering = ['price']
    paginate_by = 12

    def get_queryset(self):
        self.cat = get_object_or_404(Category, id=self.kwargs['cat_id'])
        return self.cat.products.all()

# محصولات بر اساس برچسب ها


class SortByTagView(ListView):
    template_name = 'products/productsList.html'
    model = Product
    context_object_name = 'products'
    ordering = ['price']
    paginate_by = 12

    def get_queryset(self):
        tag = self.kwargs['tag']
        return Product.objects.filter(product_tag__tag=tag, is_active=True)  
    

# سایدبار فیلتر محصولات
def sideBar_filter(request):
    categories = Category.objects.all()
    tags = ProductTags.all()
    context = {'categories': categories, 'tags': tags}
    return render(request, 'products/sidebar_filter.html', context)