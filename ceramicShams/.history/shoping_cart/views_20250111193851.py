from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.http import JsonResponse
from products.models import Product
from .models import Cart, Order



# Create your views here.


# افزودن به سبد خرید
def add_to_cart(request: HttpRequest):
    product_id = request.GET.get('product_id')
    count = request.GET.get('count')

    # بررسی مقدار count
    if count is None or not count.isdigit() or int(count) < 1:
        return JsonResponse({
            "error": "تعداد وارد شده معتبر نیست"
        }, status=400)

    # بررسی احراز هویت کاربر
    if not request.user.is_authenticated:
        return JsonResponse({
            "error": "برای افزودن محصول به سبد خرید ابتدا وارد حساب کاربری شوید."
        }, status=401)

    # بررسی وجود محصول
    product = Product.objects.filter(id=product_id, is_active=True).first()
    if product is None:
        return JsonResponse({
            "error": "محصول مورد نظر یافت نشد یا غیرفعال است."
        }, status=404)

    # یافتن یا ایجاد سبد خرید کاربر
    current_cart, create = Cart.objects.get_or_create(
        user_id=request.user.id, payment=False
    )

    # بررسی وجود سفارش قبلی برای همین محصول
    current_order = current_cart.order.filter(product_id=product_id).first()
    if current_order is not None:
        current_order.count += int(count)
        current_order.save()
    else:
        new_order = Order(cart_id=current_cart.id,
                          product_id=product_id, count=int(count))
        new_order.save()

    # پاسخ موفقیت‌آمیز
    return JsonResponse({
        'success': 'محصول مورد نظر به سبد خرید شما اضافه شد'
    })

def CartView(request):
    Order = Cart.order.filter(user_id = re)

    
