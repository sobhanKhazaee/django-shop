from django.shortcuts import render
import class NameView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('GET request!')

    def post(self, request, *args, **kwargs):
        return HttpResponse('POST request!')
# Create your views here.

def 
