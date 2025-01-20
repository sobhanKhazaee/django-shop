from django.shortcuts import render
from django.views.generic import TemplateView, View
from account.models import User
from .forms import profile_model_Form, ChangePasswordForm



# Create your views here.

# صفحه اصلی داشبورد
class DashboardView(TemplateView):
    template_name = 'dashboard.html'

# رندر کردن سایدبار
def user_panel_menu_component(request):
    return render(request, 'component/sidebar.html')

# ویرایش پروفایل
class EditProfileView(View):
    def get(self, request):
        current_user = User.objects.get(id=request.user.id)
        edit_form = profile_model_Form(instance=current_user)
        context = {
            'form': edit_form,
            'current_user': current_user
        }
        return render(request, "edit_profile.html", context)
    def post(self, request):
        current_user = User.objects.get(id=request.user.id)
        edit_form = profile_model_Form(request.POST, instance=current_user)
        if edit_form.is_valid():
            edit_form.save()
            return render(request, "edit_profile.html", {'form': edit_form, 'current_user': current_user})
        else:
            return render(request, "edit_profile.html", {'form': edit_form, 'current_user': current_user})
        
        
# تغییر رمز عبور
class ChangePasswordView(View):
    def get(self, request):
        context = {
            'form': ChangePasswordForm()
        }
        return render(request, "change_password.html", context)
    def post(self, request):
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            current_user = User.objects.get(id=request.user.id)
            if current_user.check_passw
            return render(request, "change_password.html")
        else:
            return render(request, "change_password.html", {'form': form})
       