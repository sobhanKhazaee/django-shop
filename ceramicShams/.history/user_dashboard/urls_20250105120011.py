from django.urls import path
from . import views

urlpatterns = [
    path('', views.DashboardView.as, name='dashboard_page'),
]

