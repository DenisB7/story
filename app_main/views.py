from django.shortcuts import render, redirect
from django.views import View
from app_main.models import CompanyCruise

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
        return render(request, 'app_main/survey.html')

    def post(self, request):
        company_name = request.POST.get('company')
        justification = request.POST.get('justification')
        user_id = request.user.pk
        result_of_survey_save = (
            CompanyCruise.objects
            .filter(user_id=user_id)
            .update(
                name=company_name,
                justification=justification,
            )
        )
        return redirect('app_main:survey')
