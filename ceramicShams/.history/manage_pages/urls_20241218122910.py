from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_page),
    path('about_us', views.about_us,name='about'),
    path('contact_us', views.contact_us),
]
