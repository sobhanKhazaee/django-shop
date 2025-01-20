from django.urls import path
from . import views

urlpatterns = [
    path('',views.index_page),
    path('about_us',views.index_page),
    path('contact',views.index_page),
]
