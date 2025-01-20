from django.shortcuts import render
fro

# Create your views here.

def contact_us(request):
    
    return render(request, 'contactUs/contact_us.html')
