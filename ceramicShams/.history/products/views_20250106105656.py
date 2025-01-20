from django.shortcuts import render, get_object_or_404
from .models import Product, Category, Brand
from django.db.models import Avg
from django.views.generic import ListView, DetailView
from django.http import JsonResponse

# Create your views here.

# لیست  همه ی محصولات


class productsListView(ListView):
    template_name = 'products/productsList.html'
    model = Product
    context_object_name = 'products'
    ordering = ['price']
    paginate_by = 8

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
    paginate_by = 8

    def get_queryset(self):
        self.cat = get_object_or_404(Category, id=self.kwargs['cat_id'])
        return self.cat.products.all()

# محصولات بر اساس برند


class SortByBrandView(ListView):
    template_name = 'products/productsList.html'
    model = Product
    context_object_name = 'products'
    ordering = ['price']
    paginate_by = 8

    def get_queryset(self):
        self.brand = get_object_or_404(Brand, id=self.kwargs['brand_id'])
        return self.brand.brand_products.all()

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
    brand = Brand.objects.all()
    max_price = Product.objects.all().order_by('-price').first().price
    min_price = Product.objects.all().order_by('price').first().price
    context = {
        'categories': categories,
        'brands': brand,
        'max_price': max_price,
        'min_price': min_price,
    }
    return render(request, 'products/components/sidebar_filter.html', context)





class FilterByPriceView(ListView):
    template_name = 'products/productsList.html'
    model = Product
    context_object_name = 'products'
    paginate_by = 8

    def get_queryset(self):
        max_price = self.request.GET.get('price_range')
        if max_price:
            try:
                max_price = int(max_price)
                return Product.objects.filter(price__lte=max_price)
            except ValueError:
                pass  # اگر مقدار غیر معتبر ارسال شود، فقط خطا را رد می‌کنیم
        # مقدار پیش‌فرض: بازگشت همه محصولات
        return Product.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['min_price'] = Product.objects.all().order_by('price').first().price or 0
        context['max_price'] = Product.objects.all().order_by('-price').first().price or 1000000
        return context

