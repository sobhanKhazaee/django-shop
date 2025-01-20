from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class DashboardView(TemplateView):
    template_name = 'dashboard.html'
    
def user_panel_menu_component(request):
    return render(request, 'components/user_panel_menu_component.html')    
