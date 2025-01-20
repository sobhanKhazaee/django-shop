from django.shortcuts import render
from django.http import HttpRequest
from django.http import JsonResponse
from products import msd



# Create your views here.

def add_to_cart(request: HttpRequest):
    product_id = request.GET.get('product_id')
    count = request.GET.get('count')
    
    if count is None or int(count) < 1:
        return JsonResponse({
            "error": "تعداد وارد شده معتبر نیست"
        }, status=400)
