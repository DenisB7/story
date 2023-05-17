from django.urls import path

from app_main.views import MainView, SurveyView


app_name = "app_main"
urlpatterns = [
    path('', MainView.as_view(), name="main"),
    path('survey', SurveyView.as_view(), name="survey"),
]
