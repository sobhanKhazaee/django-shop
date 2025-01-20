from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from account.models import User
from .forms import profile_model_Form, ChangePasswordForm
from django.contrib.auth import logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
import zibal.zibal as zibal
from django.conf import settings



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

# ایجاد پرداخت
def create_payment(request):
    merchant_id = settings.ZIBAL_MERCHANT_ID
    callback_url = settings.ZIBAL_CALLBACK_URL
    zb = zibal.zibal(merchant_id, callback_url)

    amount = 30000  # مبلغ به ریال
    response = zb.request(amount)
    result_code = response['result']

    if result_code == 100:  # کد موفقیت
        track_id = response['trackId']
        return redirect(f"https://gateway.zibal.ir/start/{track_id}")
    else:
        return render(request, 'error.html', {'message': zb.request_result(result_code)})
    



def verify_payment(request):
    merchant_id = settings.ZIBAL_MERCHANT_ID
    zb = zibal.zibal(merchant_id, None)

    track_id = request.GET.get('trackId')  # از پارامتر بازگشتی زیبال دریافت کنید
    verify_response = zb.verify(track_id)
    result_code = verify_response['result']

    if result_code == 100:  # تایید موفقیت‌آمیز
        ref_number = verify_response['refNumber']
        return JsonResponse({'status': 'success', 'refNumber': ref_number})
    else:
        return JsonResponse({'status': 'error', 'message': zb.verify_result(result_code)})    
