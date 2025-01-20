from django.urls import path
from . import views

urlpatterns = [
    path('', views.contactUsView.class NameView(View):
        def get(self, request, *args, **kwargs):
            return HttpResponse('GET request!')
    
        def post(self, request, *args, **kwargs):
            return HttpResponse('POST request!'), name='contact_us'),
]
