from django.shortcuts import render
from django.contrib.auth import get_user_model
fro

# Create your views here.

# user = get_user_model()
class registerView(View):
    def get(self):
        return HttpResponse('GET request!')

    def post(self, request):
        return HttpResponse('POST request!')