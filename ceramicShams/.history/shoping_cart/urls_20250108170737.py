from django.urls import path
from . import views

urlpatterns = [
    
   path('add-to', views.your_view, name='your_view_name'),
]