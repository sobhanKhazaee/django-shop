from django.shortcuts import render
from products.models import Category
from django.views.generic.base import TemplateView
from banner.models import Banner
from products.models import Product
from site_setting.models import SiteSetting

class indexPageView(TemplateView):
    template_name = 'manage_pages/indexpage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['banners'] = Banner.objects.filter(active=True )
        context["products"] = Product.objects.all()
        return context


def header_partial(request):
    
    cats = Category.objects.all()
    return render(request, 'layout/header.html', {
        "cats": cats,
        'set':set
    })
    
def head_partial(request):
    set = SiteSetting.objects.first()
    return render(request, 'layout/header.html', {
        "cats": cats,
        'set':set
    })


class aboutUsView(TemplateView):
    template_name = 'manage_pages/about_us.html'

