from django.urls import path
from . import views

urlpatterns = [
    path('',views.index_page),
    path('about ',views.index_page),
    path('',views.index_page),
]
