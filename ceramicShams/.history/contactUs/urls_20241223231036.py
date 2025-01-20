from django.urls import path
from . import views

urlpatterns = [
    path('', views.contactUsView.ve, name='contact_us'),
]
