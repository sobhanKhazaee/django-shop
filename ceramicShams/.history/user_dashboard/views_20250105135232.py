from django.shortcuts import render
from django.views.generic import TemplateView,View


# Create your views here.
class DashboardView(TemplateView):
    template_name = 'dashboard.html'
    
def user_panel_menu_component(request):
    return render(request, 'component/sidebar.html')    
