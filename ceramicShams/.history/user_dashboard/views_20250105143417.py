from django.shortcuts import render
from django.views.generic import TemplateView, View
from account.models import User
from .forms import profile_model_Form

# Create your views here.


class DashboardView(TemplateView):
    template_name = 'dashboard.html'


def user_panel_menu_component(request):
    return render(request, 'component/sidebar.html')


class EditProfileView(View):
    def get(self, request):
        current_user = User.objects.get(id=request.user.id)
        edit_form = profile_model_Form(instance=current_user)
        context = {
            'form': edit_form,
            'current_user': current_user
        }
        return render(request,edit_profile)
