from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import Http404, HttpRequest
from django.views.generic import View
from .models import User
from .forms import RegisterForm, LoginForm, ForgetPassForm, ResetPaswordForm
from django.utils.crypto import get_random_string
from django.contrib.auth import login, logout
from utils.email_service import send_email

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
            entered_user_name = register_form.cleaned_data.get('user_name')
            entered_email = register_form.cleaned_data.get('email')
            entered_password = register_form.cleaned_data.get('password')
            user: bool = User.objects.filter(
                email__iexact=entered_email).exists()
            if user:
                register_form.add_error("این ایمیل قبلا ثبت شده است")
            else:
                new_user = User(
                    username=entered_user_name,
                    is_active=False,
                    email=entered_email,
                    email_active_code=get_random_string(72)
                )
                new_user.set_password(entered_password)
                send_email("فعالسازی حساب کاربری", new_user.email, {
                           "user": new_user}, "email/active_account.html")
                new_user.save()
                return redirect(reverse('login_page'))

        else:
            context = {
                'register_form': register_form
            }
            # print("form invalid")
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
        if login_form.is_valid():
            user_email = login_form.cleaned_data.get('email')
            user_password = login_form.cleaned_data.get('password')
            user = User.objects.filter(email__iexact=user_email).first()
            if user is not None:
                pass_correct = user.check_password(user_password)
                if not pass_correct:
                    login_form.add_error('email', "رمز عبور شما صحیح نمیباشد")
                elif not user.is_active:
                    login_form.add_error('email', 'حساب کاربری شما فعال نیست')
                else:
                    login(request, user)
                    return redirect(reverse('index_page'))

        else:
            context = {
                'login': login_form
            }
            return render(request, "login.html", context)

# log out

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse("index_page"))

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


# فراموشی رمز عبور

class ForgetPasswordView(View):
    def get(self, request: HttpRequest):
        forget_form = ForgetPassForm()
        context = {"forget": forget_form}
        return render(request, "forget_pass.html", context)

    def post(self, request: HttpRequest):
        forget_form = ForgetPassForm(request.POST)
        if forget_form.is_valid():
            user_email = forget_form.cleaned_data.get('email')
            user = User.objects.filter(email__iexact=user_email).first()
            if user is not None:
                send_email("بازیابی رمز عبور", user_email, {'user': user}, "email/forget_password.html")
                context = {"forget": forget_form}
                return render(request, "forget_pass.html", context)
            else:
                forget_form.add_error(
                    "email", "با این ایمیل ثبت نامی صورت نگرفته است")
        else:
            context = {"forget": forget_form}
            return render(request, "forget_pass.html", context)




class ResetPasswordView(View):
    def get(self, request, active_code):
        user = User.objects.filter(
            email_active_code__iexact=active_code).first()
        if user is None:
            return redirect(reverse("login_page"))
        else:
            reset_form = ResetPaswordForm()
            context = {
                "reset_form": reset_form,
                "user": user
            }
            return render(request, "reset_pass.html", context)

    def post(self, request, active_code):
        reset_form = ResetPaswordForm(request.POST)
        user = User.objects.filter(
            email_active_code__iexact=active_code).first()
        if reset_form.is_valid():
            if user is not None:
                new_password = reset_form.cleaned_data.get("password")
                user.set_password(new_password)
                user.is_active = True
                user.email_active_code = get_random_string(72)
                user.save()
                return redirect(reverse("login_page"))

        else:
            context = {
                "reset_form": reset_form,
                "user": user
            }
            return render(request, "reset_pass.html", context)
