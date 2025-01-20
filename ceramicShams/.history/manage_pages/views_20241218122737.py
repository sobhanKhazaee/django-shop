from django.shortcuts import render
from products.models import Category

# Create your views here.


def index_page(request):
    return render(request, 'manage_pages/indexpage.html')


def header_partial(request):
    cats = Category.objects.all()
    return render(request, 'layout/header.html', {
        "cats": cats
    })
    
def about_us(request):
    return render(request, 'manage_pages/about_us.html')        
def about_us(request):
    return render(request, 'manage_pages/about_us.html')        
