from django.shortcuts import render
# from django.contrib.auth import get_user_model
from django.views.generic import View
from .forms import RegisterForm

# Create your views here.

# user = get_user_model()


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
            entered_email = register_form.cleaned_data.get("ema")
            
        context = {
            'register_form': register_form
        }
