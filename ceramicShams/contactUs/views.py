from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import contact_model_Form
from django.views.generic.edit import CreateView


# Create your views here.


class contactUsView(CreateView):
    template_name = 'contactUs/contact_us.html'
    form_class = contact_model_Form
    success_url = reverse_lazy('contact_us')




       
