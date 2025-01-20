from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.views.generic import View

# Create your views here.

# user = get_user_model()
class egisterView(View):
    def get(self):
        return HttpResponse('GET request!')

    def post(self, request):
        return HttpResponse('POST request!')