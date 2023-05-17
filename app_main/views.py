from django.shortcuts import render, redirect
from django.views import View

from django.contrib.auth.mixins import LoginRequiredMixin

class MainView(View):

    def get(self, request):
        return render(request, 'app_main/main.html', {'username': request.user.username})


class SurveyView(LoginRequiredMixin, View):

    def test_func(self):
        return self.request.user.is_authenticated

    def handle_no_permission(self):
        return redirect("app_main:main")

    def get(self, request):
        return render(request, 'app_main/survey.html', {'username': request.user.username})
