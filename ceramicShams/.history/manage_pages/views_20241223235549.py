from django.shortcuts import render
from products.models import Category
from django.views import View
from django.views.generic.base import TemplateView


# Create your views here.


class indexPageView(TemplateView):
    template_name = 'manage_pages/indexpage.html'

class headerPartial(TemplateView):
    template_name = 'layout/header.html'
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context["cats"] = 
        return context
    


def header_partial(request):
    cats = Category.objects.all()
    return render(request, 'layout/header.html', {
        "cats": cats
    })
    
class aboutUsView(TemplateView):
    template_name = 'manage_pages/about_us.html'

# def about_us(request):
#     return render(request, 'manage_pages/about_us.html')
