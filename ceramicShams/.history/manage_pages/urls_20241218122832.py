from django.urls import path
from . import views

urlpatterns = [
    path('',views.index_page),
    path('about_',views.index_page),
    path('',views.index_page),
]
