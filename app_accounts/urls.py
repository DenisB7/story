from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from app_accounts.views import MainView

app_name = 'app_accounts'
urlpatterns = [
    path('', MainView.as_view(), name="main"),
    path("login", LoginView.as_view(template_name="app_accounts/login.html"), name="login"),
    path("logout", LogoutView.as_view(), name="logout"),
]
