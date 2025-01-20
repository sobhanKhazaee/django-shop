from django.shortcuts import render
from .forms import 

# Create your views here.


def contact_us(request):
    if request.method == 'post'
        obj_contact_form = contactForm()
        return render(request, 'contactUs/contact_us.html', {
            'contact_form': obj_contact_form
        })
