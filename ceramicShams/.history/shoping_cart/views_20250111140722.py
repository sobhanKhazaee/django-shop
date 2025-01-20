from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Cart, Order
from products.models import Product

def add_to_cart(request):
    product_id = request.GET.get('product_id')
    count = request.GET.get('count')

    if not count or int(count) < 1:
        return JsonResponse({
            "error": "تعداد وارد شده معتبر نیست"
        }, status=400)

    if not request.user.is_authenticated:
        return JsonResponse({
            "error": "برای افزودن محصول به سبد خرید ابتدا وارد حساب کاربری خود شوید."
        }, status=401)

    product = Product.objects.filter(id=product_id, is_active=True).first()
    if not product:
        return JsonResponse({
            "error": "محصول مورد نظر یافت نشد یا غیرفعال است."
        }, status=404)

    current_cart, created = Cart.objects.get_or_create(
        user=request.user,
        payment=False
    )

    current_order = current_cart.order.filter(product_id=product_id).first()
    if current_order:
        current_order.count += int(count)
        current_order.save()
    else:
        Order.objects.create(
            cart=current_cart,
            product=product,
            count=int(count)
        )

    return JsonResponse({
        "success": "محصول با موفقیت به سبد خرید اضافه شد."
    })
