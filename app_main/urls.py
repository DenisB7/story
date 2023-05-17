from django.urls import path

from app_main.views import MainView


app_name = "app_main"
urlpatterns = [
    path('', MainView.as_view(), name="main"),
]
