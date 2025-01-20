from django.urls import path
from . import views

urlpatterns = [
    path('', views.contactUsView.as, name='contact_us'),
]
