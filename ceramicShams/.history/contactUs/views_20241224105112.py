from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import contact_model_Form
from django.views.generic.edit import FormView
from django.contrib import messages


# Create your views here.


class contactUsView(FormView):
    template_name = 'contactUs/contact_us.html'
    form_class = contact_model_Form
    success_url = reverse_lazy('contact_us')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "پیام شما با موفقیت ارسال شد.")
        return super().form_valid(form)

    def form_invalid(self, form):
        con
