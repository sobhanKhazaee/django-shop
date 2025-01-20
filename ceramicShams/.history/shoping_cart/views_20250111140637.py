from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.http import JsonResponse
from products.models import Product
from .models import Cart, Order


# Create your views here.

def add_to_cart(request: HttpRequest):
    product_id = request.GET.get('product_id')
    count = request.GET.get('count')

    if count is None or int(count) < 1:
        return JsonResponse({
            "error": "تعداد وارد شده معتبر نیست"
        }, status=400)

    if request.user.is_authenticated:
             return JsonResponse({
            "error": "برای افزودن محصول به سبد خرید ابتدا وارد حساب کاربری خود شوید."
        }, status=401)

        product = Product.objects.filter(id=product_id, is_active=True).first
        if product is not None:
            current_cart, create = Cart.objects.get_or_create(
                user_id=request.user.id, payment=False)
            current_order = current_cart.order.filter(
                product_id=product_id).first()
            if current_order is not None:
                current_order.count += int(count)
                current_order.save()
            else:
                new_order = Order(cart_id=current_cart.id,
                                  product_id=product_id, count=count)
                print(new_order)
                new_order.save()
                return JsonResponse({
                    'success': 'محصول مورد نظر به سبد خرید شما اضافه شد',
                })
