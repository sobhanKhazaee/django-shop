from django.shortcuts import render
from .forms import contact_model_Form

# Create your views here.


def contact_us(request):
    if request.method == 'post'
    pass
    else:
        obj_contact_form = contactForm()
        return render(request, 'contactUs/contact_us.html', {
            'contact_form': obj_contact_form
        })
