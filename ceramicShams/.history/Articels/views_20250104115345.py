from django.shortcuts import render
from .models import ArticelCategories, Aticel
from django.views.generic import ListView,DetailView
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

    def get_queryset(self):
        query = super(ArticelsListView, self).get_queryset()
        query = query.filter(is_active=True)
        category_name = self.kwargs.get('category')
        if category_name is not None:
            query = query.filter(category__url__iexact=category_name)
        return query    
    
class ArticelDetailsView(DetailView):    
    template_name = 'articel_details.html'
    model = Aticel
    context_object_name = "articel"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        contextج
        context['categories'] = ArticelCategories.objects.all()
        return context
    

            
