from django.urls import path
from . import views

urlpatterns = [
    path('', views.contactUsView, name='contact_us'),
]
