from django.shortcuts import render
from .forms import contactForm

# Create your views here.

def contact_us(request):
    obj_contact_form =contactForm()
    return render(request, 'contactUs/contact_us.html',{
        
    })
