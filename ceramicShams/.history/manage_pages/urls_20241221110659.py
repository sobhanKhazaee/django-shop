from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_page,name='index_page'),
    path('about_us', views.about_us, name='about_us'),
  
]
