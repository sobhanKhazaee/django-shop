from django.urls import path
from . import views

urlpatterns = [
    path('', views.mangePagesView.as_view,name='index_page'),
    path('about_us', views.about_us, name='about_us'),
  
]
