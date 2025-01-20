from django.views.generic.base import TemplateView
from banner.models import Banner

class indexPageView(TemplateView):
    template_name = 'manage_pages/indexpage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # اضافه کردن بنرهای فعال به کانتکست
        context['banners'] = Banner.objects.filter(active=True)
        return context


def header_partial(request):
    cats = Category.objects.all()
    return render(request, 'layout/header.html', {
        "cats": cats
    })


class aboutUsView(TemplateView):
    template_name = 'manage_pages/about_us.html'

