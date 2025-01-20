from django.shortcuts import render
from django.views.generic import TemplateView,View
from account.models import User

# Create your views here.
class DashboardView(TemplateView):
    template_name = 'dashboard.html'
    
def user_panel_menu_component(request):
    return render(request, 'component/sidebar.html')    

class EditProfileView(View):
    def get(self, request):
        current_user = User.objects.filter(id=request.user.id).first()
        context = {
            'current_user': current_user
        }
        return render(request, 'edit_profile.html', context)
    
    def post(self, request):
        current_user = User.objects.filter(id=request.user.id).first()
        current_user.first_name = request.POST.get('first_name')
        current_user.last_name = request.POST.get('last_name')
        current_user.email = request.POST.get('email')
        current_user.save()
        context = {
            'current_user': current_user
        }
        return render(request, 'edit_profile.html', context)
