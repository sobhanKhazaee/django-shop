from django.shortcuts import render
from .forms import contact_model_Form
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView



# Create your views here.


class contactUsView(View):
    def get(self, request):
        obj_contact_form = contact_model_Form()
        return render(request, 'contactUs/contact_us.html', {
            'contact_form': obj_contact_form
        })
    
        template_name = 'contactUs/contact_us.html'
    def def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["contact_form"] = 
        return context
    

    def post(self, request):
        obj_contact_form = contact_model_Form(request.POST)
        if obj_contact_form.is_valid():
            obj_contact_form.save()
            return HttpResponse('تیکت شما با موفقیت ثبت شد')
        else:
            return render(request, 'contactUs/contact_us.html', {
                'contact_form': obj_contact_form
            })


# def contact_us(request):
#     if request.method == 'POST':
#         obj_contact_form = contact_model_Form(request.POST)
#         if obj_contact_form.is_valid():
#             obj_contact_form.save()
#             return HttpResponse('تیکت شما با موفقیت ثبت شد')
#         else:
#             return render(request, 'contactUs/contact_us.html', {
#                 'contact_form': obj_contact_form
#             })
#     else:
#         obj_contact_form = contact_model_Form()
#         return render(request, 'contactUs/contact_us.html', {
#             'contact_form': obj_contact_form
#         })
