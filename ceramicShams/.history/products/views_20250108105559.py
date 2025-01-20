from django.shortcuts import render, get_object_or_404
from .models import Product, Category, Brand
from django.db.models import Avg, Q
from django.views.generic import ListView, DetailView
from django.http import JsonResponse
from utils.helpers import get_client_ip

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


# فیلتر محصولات بر اساس قیمت
class FilterByPriceView(ListView):
    template_name = 'products/productsList.html'
    model = Product
    context_object_name = 'products'
    ordering = ['price']
    paginate_by = 8

    def get_queryset(self):
        queryset = super().get_queryset()

        # پارامترهای ورودی از درخواست
        max_price = self.request.GET.get('price_range')
        category_id = self.request.GET.get('category')
        brand_id = self.request.GET.get('brand')
        tag = self.request.GET.get('tag')

        # فیلترهای ترکیبی
        filters = Q()

        if max_price:
            try:
                filters &= Q(price__lte=int(max_price))
            except ValueError:
                pass

        if category_id:
            filters &= Q(category__id=category_id)

        if brand_id:
            filters &= Q(brand__id=brand_id)

        if tag:
            filters &= Q(product_tag__tag=tag)

        return queryset.filter(filters).distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # ارسال پارامترهای فعلی به قالب
        context['current_filters'] = self.request.GET.dict()
        return context

# جزئیات محصول


class productDetailsView(DetailView):
    template_name = 'products/productDetails.html'
    model = Product
    context_object_name = "product"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = self.object.product_tag.all()
        user_ip = get_client_ip(self.request)
        user_id = None
        if self.request.user.is_authenticated:
            user_id = self.request.

        return context
