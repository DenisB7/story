from django.shortcuts import render
from django.views import View

from django.contrib.auth.mixins import LoginRequiredMixin

class MainView(View):

    def get(self, request):
        return render(request, 'app_main/main.html', {'username': request.user.username})


class SurveyView(LoginRequiredMixin, View):

    def get(self, request):
        return render(request, 'app_main/survey.html', {'username': request.user.username})
