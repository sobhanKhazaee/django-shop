from django.shortcuts import render
from django.http import HttpRequest



# Create your views here.

def add_to_cart(request:HttpRequest):
    product_id = request.GET.get('product_id')
    count = request.GET.get('count')
    # print(f"product_id = {product_id} \n count = {count}")
    if count < 1 :
   