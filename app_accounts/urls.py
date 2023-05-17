from django.urls import path

from app_accounts.views import MainView

app_name = 'app_accounts'
urlpatterns = [
    path('', MainView.as_view(), name="main"),
]
