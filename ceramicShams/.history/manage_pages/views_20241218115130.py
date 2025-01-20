from django.shortcuts import render

# Create your views here.

def index_page(request):
    return render(request,'manage_ages/indexpage.html')

def heade