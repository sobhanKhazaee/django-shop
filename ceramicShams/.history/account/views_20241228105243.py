from django.shortcuts import render
from django.contrib.auth import get_user_model

# Create your views here.

# user = get_user_model()
class registerView(class NameView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('GET request!')

    def post(self, request, *args, **kwargs):
        return HttpResponse('POST request!'))