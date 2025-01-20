from django.shortcuts import render
from products.models import Category
from django.views import View
from django.views.generic.base import TemplateView


# Create your views here.


class indexPageView(View):
    template_name = 'manage_pages/indexpage.html'
    def get(self,request):
         return render(request, self.template_name)
        
class NameView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('GET request!')

    def post(self, request, *args, **kwargs):
        return HttpResponse('POST request!')

def header_partial(request):
    cats = Category.objects.all()
    return render(request, 'layout/header.html', {
        "cats": cats
    })


def about_us(request):
    return render(request, 'manage_pages/about_us.html')



