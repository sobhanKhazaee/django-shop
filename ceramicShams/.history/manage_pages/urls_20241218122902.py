from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_page),
    path('about_us', views.about_us,nam),
    path('contact_us', views.contact_us),
]
