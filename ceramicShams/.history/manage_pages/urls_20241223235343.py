from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexPageView.as_view(),name='index_page'),
    path('about_us', views.aboutUsView.as_view(), name='about_us'),
  
]
