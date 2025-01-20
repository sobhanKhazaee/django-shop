from django.shortcuts import render, redirect
from django.views.generic import View
from .models import User
from .forms import RegisterForm
from django.utils.crypto import get_random_string
from django.urls import reverse
# Create your views here.


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        context = {
            'register_form': register_form
        }
        return render(request, "register.html", context)

    def post(self, request):
        register_form = RegisterForm()
        if register_form.is_valid():
            entered_email = register_form.cleaned_data.get('email')
            entered_password = register_form.cleaned_data.get('password')
            user: bool = User.objects.filter(
                email__iexact=entered_email).exists()
            if user:
                register_form.add_error("این ایمیل قبلا ثبت شده است")
            else:
                new_user = User(
                    is_active=False,
                    email=entered_email,
                    email_active_code=get_random_string(72)
                )
                new_user.set_password(entered_password)
                new_user.save()
                return redirect(re)
        else:
            context = {
                'register_form': register_form
            }
            return render(request, "register.html", context)
