from django.urls import path
from . import views

urlpatterns = [
    path('', views.DashboardView.as_view(), name='dashboard_page'),
    path('editprofile', views.DashboardView.as_view(), name='editprofile'),
]

