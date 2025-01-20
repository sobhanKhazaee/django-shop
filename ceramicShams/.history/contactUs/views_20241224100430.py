from django.shortcuts import render
from .forms import contact_model_Form

from django.views.generic.edit import FormView


# Create your views here.


class contactUsView(FormView):
    template_name = 'contactUs/contact_us.html'
    form_class = contact_model_Form
    success_url = 'contact_us'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    # def get(self, request):
    #     obj_contact_form = contact_model_Form()
    #     return render(request, 'contactUs/contact_us.html', {
    #         'contact_form': obj_contact_form
    #     })

    # def post(self, request):
    #     obj_contact_form = contact_model_Form(request.POST)
    #     if obj_contact_form.is_valid():
    #         obj_contact_form.save()
    #         return HttpResponse('تیکت شما با موفقیت ثبت شد')
    #     else:
    #         return render(request, 'contactUs/contact_us.html', {
    #             'contact_form': obj_contact_form
    #         })


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
