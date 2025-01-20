from django.urls import path
from . import views

urlpatterns = [
    path('', views.contactUsView.a, name='contact_us'),
]
