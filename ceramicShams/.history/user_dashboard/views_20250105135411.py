from django.shortcuts import render
from django.views.generic import TemplateView,View
from account.models import User

# Create your views here.
class DashboardView(TemplateView):
    template_name = 'dashboard.html'
    
def user_panel_menu_component(request):
    return render(request, 'component/sidebar.html')    

class EditProfileView(View):
  def get(self,request):
      current_user = User.
