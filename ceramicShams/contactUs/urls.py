from django.urls import path
from . import views

urlpatterns = [
    path('', views.contactUsView.as_view(), name='contact_us'),
]
