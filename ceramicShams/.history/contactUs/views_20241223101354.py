from django.shortcuts import render
from .forms import contact_model_Form

# Create your views here.


def contact_us(request):
    if request.method == 'POST':
        obj_contact_form = contact_model_Form(request.POST)
        if
    else:
        obj_contact_form = contact_model_Form()
        return render(request, 'contactUs/contact_us.html', {
            'contact_form': obj_contact_form
        })
