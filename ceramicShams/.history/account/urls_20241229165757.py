from django.urls import path
from . import views

urlpatterns = [
    path("register", views.RegisterView.as_view(), name="register_page"),
    path("login", views.LoginView.as_view(), name="login_page"),
    path("active-account/<email_active_code>",
         views.ActiveAccountView.as_view(), name="active_account_page"),
    path("forget-password",vie)
    path("reset-password",)

]
