from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View ,ListView
from account.models import User
from .forms import profile_model_Form, ChangePasswordForm
from django.contrib.auth import logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from shoping_cart.models import Order,Cart



# Create your views here.

# صفحه اصلی داشبورد
@method_decorator(login_required, name='dispatch')
class DashboardView(TemplateView):
    template_name = 'dashboard.html'

# رندر کردن سایدبار

@login_required
def user_panel_menu_component(request):
    return render(request, 'component/sidebar.html')

# ویرایش پروفایل

@method_decorator(login_required, name='dispatch')
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
        edit_form = profile_model_Form(request.POST, request.FILES, instance=current_user)
        if edit_form.is_valid():
            edit_form.save()
            return render(request, "edit_profile.html", {'form': edit_form, 'current_user': current_user})
        else:
            return render(request, "edit_profile.html", {'form': edit_form, 'current_user': current_user})


# تغییر رمز عبور
method_decorator(login_required, name='dispatch')
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
            if current_user.check_password(form.cleaned_data.get('old_password')):
                current_user.set_password(
                    form.cleaned_data.get('new_password'))
                current_user.save()
                logout(request)
                return redirect(reverse('login_page'))
            else:
                form.add_error('old_password', 'کلمه غبور قبلی اشتباه است')
                return render(request, "change_password.html", {'form': form})

        else:
            return render(request, "change_password.html", {'form': form})

class FactorsView(ListView):
    template_name = 'factors.html'
    model = Cart
    context_object_name = 'carts'
    def get_queryset(self):
        return Cart.objects.filter(user_id=self.request.user.id, payment=True)

    def get
    