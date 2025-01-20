from django.shortcuts import render
from products.models import Category
from django.views import View

# Create your views here.


class mangePagesView()

def index_page(request):
    return render(request, 'manage_pages/indexpage.html')


def header_partial(request):
    cats = Category.objects.all()
    return render(request, 'layout/header.html', {
        "cats": cats
    })


def about_us(request):
    return render(request, 'manage_pages/about_us.html')



