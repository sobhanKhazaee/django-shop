from django.shortcuts import render
from .forms import contact_model_Form
from django.http import HttpResponse

# Create your views here.


class contactUs

def contact_us(request):
    if request.method == 'POST':
        obj_contact_form = contact_model_Form(request.POST)
        if obj_contact_form.is_valid():
            obj_contact_form.save()
            return HttpResponse('تیکت شما با موفقیت ثبت شد')
        else:
            return render(request, 'contactUs/contact_us.html', {
                'contact_form': obj_contact_form
            })
    else:
        obj_contact_form = contact_model_Form()
        return render(request, 'contactUs/contact_us.html', {
            'contact_form': obj_contact_form
        })
