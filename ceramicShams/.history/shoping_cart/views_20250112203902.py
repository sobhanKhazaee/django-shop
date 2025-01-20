from django.shortcuts import render, redirect
from django.http import HttpRequest, JsonResponse, HttpResponse
from products.models import Product
from .models import Cart, Order
from django.template.loader import render_to_string
import zibal.zibal as zibal
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now

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


# نمایش صفحه خرید


def CartView(request):
    current_cart, create = Cart.objects.select_related('user').get_or_create(
        user_id=request.user.id, payment=False)
    orders = current_cart.order.all()
    total_price = current_cart.total_price()

    context = {
        'orders': orders,
        'total_price': total_price,
    }
    return render(request, 'cart.html', context)


# حذف از سبد خرید

def remove_from_cart(request):
    product_id = request.GET.get('product_id')
    if not product_id:
        return JsonResponse({'error': 'شناسه محصول ارسال نشده است'}, status=400)

    order_count, order_dict = Order.objects.filter(
        cart__user_id=request.user.id, product_id=product_id, cart__payment=False).delete()

    if order_count == 0:
        return JsonResponse({'error': 'سفارش مورد نظر یافت نشد'}, status=404)

    current_cart, create = Cart.objects.get_or_create(
        user_id=request.user.id, payment=False)
    orders = current_cart.order.all()
    # مجموع سبد خرید
    total_price = current_cart.total_price()

    context = {
        'orders': orders,
        'total_price': total_price,
    }

    html = render_to_string('include/cart_partial.html', context)
    return JsonResponse({
        'success': 'سفارش مورد نظر از سبد خرید شما حذف شد',
        'html': html
    })


# افزایش و کاهش تعداد محصول

def add_count(request):
    product_id = request.GET.get("product_id")
    state = request.GET.get("state")
    if not product_id:
        return JsonResponse({'error': 'شناسه محصول ارسال نشده است'}, status=400)

    try:
        order = Order.objects.get(
            product_id=product_id, cart__user_id=request.user.id, cart__payment=False)
        if state == 'add':
            order.count += 1
            order.save()
        elif state == 'reduce':
            if order.count != 1:
                order.count -= 1
                order.save()
    except Order.DoesNotExist:
        return JsonResponse({'error': 'سفارش مورد نظر یافت نشد'}, status=404)

    current_cart, create = Cart.objects.get_or_create(
        user_id=request.user.id, payment=False)
    orders = current_cart.order.all()
    # مجموع سبد خرید
    total_price = current_cart.total_price()

    context = {
        'orders': orders,
        'total_price': total_price,
    }

    html = render_to_string('include/cart_partial.html', context)
    return JsonResponse({
        'success': 'سفارش مورد نظر از سبد خرید شما حذف شد',
        'html': html
    })


# ایجاد درگاه پرداخت
@login_required
def create_payment(request):
    merchant_id = settings.ZIBAL_MERCHANT_ID
    callback_url = settings.ZIBAL_CALLBACK_URL
    zb = zibal.zibal(merchant_id, callback_url)

    current_cart = Cart.objects.select_related('user').get(
        user_id=request.user.id, payment=False)
    total_price = current_cart.total_price()

    amount = total_price * 10  # مبلغ به ریال
    response = zb.request(amount)
    result_code = response['result']

    if result_code == 100:  # کد موفقیت
        track_id = response['trackId']
        return redirect(f"https://gateway.zibal.ir/start/{track_id}")
    else:
        return render(request, 'error.html', {'message': zb.request_result(result_code)})


# تایید پرداخت

def verify_payment(request):
    merchant_id = settings.ZIBAL_MERCHANT_ID
    zb = zibal.zibal(merchant_id, None)
    current_cart = Cart.objects.select_related('user').get(
        user_id=request.user.id, payment=False)
    
    current_cart.payment = True
    current_cart.payment_date = now()
    current_cart.save()
    
    # از پارامتر بازگشتی زیبال دریافت کنید
    track_id = request.GET.get('trackId')
    verify_response = zb.verify(track_id)
    result_code = verify_response['result']

    if result_code == 100:  # تایید موفقیت‌آمیز
        ref_number = verify_response['refNumber']
        return HttpResponse(f'پرداخت شما با موفقیت انجام شد. شماره پیگیری: {ref_number}')
    else:
        return HttpResponse(f'خطا در پرداخت: {zb.verify_result(result_code)}')
