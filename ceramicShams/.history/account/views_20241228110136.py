from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.views.generic import View

# Create your views here.

# user = get_user_model()
class RegisterView(View):
    def get(self):
        regis

    def post(self, request):
        return HttpResponse('POST request!')