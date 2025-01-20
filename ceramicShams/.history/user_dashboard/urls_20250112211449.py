from django.urls import path
from . import views

urlpatterns = [
    path('', views.DashboardView.as_view(), name='dashboard_page'),
    path('editprofile', views.EditProfileView.as_view(), name='edit_profile'),
    path('change-password', views.ChangePasswordView.as_view(), name='change_password'),
    path('', views.ChangePasswordView.as_view(), name='change_password'),
]
