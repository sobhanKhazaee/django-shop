from django.urls import path
from . import views

urlpatterns = [
    # Define your URL patterns here
   path('your-url/', views.your_view, name='your_view_name'),
]