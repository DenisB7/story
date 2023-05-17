from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from app_accounts.views import RegisterView


app_name = 'app_accounts'
urlpatterns = [
    path('register', RegisterView.as_view(), name="register"),
    path("login", LoginView.as_view(
            template_name="app_accounts/login.html",
            redirect_authenticated_user=True,
        ),
        name="login"
    ),
    path("logout", LogoutView.as_view(), name="logout"),
]
