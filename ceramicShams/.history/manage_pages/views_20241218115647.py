from django.shortcuts import render

# Create your views here.

def index_page(request):
    return render(request,'manage_pges/indexpage.html')

def header_partial(request):
    return render(request,'layout/header.html')