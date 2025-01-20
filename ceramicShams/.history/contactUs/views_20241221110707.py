from django.shortcuts import render

# Create your views here.

def contact_us(request):
    return render(request, 'manage_pages/contact_us.html')
