from django.shortcuts import render
from .forms import 

# Create your views here.

def contact_us(request):
    
    return render(request, 'contactUs/contact_us.html')
