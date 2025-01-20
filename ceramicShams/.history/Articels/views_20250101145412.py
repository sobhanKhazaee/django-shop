from django.shortcuts import render
from .models import ArticelCategories, Aticel
from django.views.generic import ListView
# Create your views here.

class ArticelsListView(ListView):
    template_name = "articels_list.html"
    model = Aticel
    context_object_name = "articels"
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ArticelCategories.objects.all()
        return context
    