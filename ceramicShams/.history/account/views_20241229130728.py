from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import Http404
from django.views.generic import View
from .models import User
from .forms import RegisterForm, LoginForm
from django.utils.crypto import get_random_string
from django.contrib.auth import login, logout

# Create your views here.

# ثبت نام


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        context = {
            'register_form': register_form
        }
        return render(request, "register.html", context)

    def post(self, request):
        register_form = RegisterForm(request.POST)
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
                return redirect(reverse('login_page'))
        else:
            context = {
                'register_form': register_form
            }
            print("form invalid")
            return render(request, "register.html", context)

# لاگین


class LoginView(View):

    def get(self, request):
        login_form = LoginForm()
        context = {
            'login': login_form
        }
        return render(request, "login.html", context)

    def post(self, request):
        login_form = LoginForm(request.POST)
        user_email = login_form.cleaned_data.get('email')
        user_password = login_form.cleaned_data.get('password')
        user = User.objects.filter
        # فعال سازی حساب کاربری


class ActiveAccountView(View):
    def get(self, request, email_active_code):
        user = User.objects.filter(
            email_active_code__iexact=email_active_code).first()
        if user is not None:
            if not user.is_active:
                user.is_active = True
                user.email_active_code = get_random_string(72)
                user.save()
                return redirect(reverse('login_page'))
            else:
                pass

        raise Http404
