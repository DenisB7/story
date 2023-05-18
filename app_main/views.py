from django.shortcuts import render, redirect
from django.views import View
from app_main.models import FavoriteCruiseCompany

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
        try:
            user_favorite_company = FavoriteCruiseCompany.objects.get(user_id=request.user.pk)
        except FavoriteCruiseCompany.DoesNotExist:
            user_favorite_company = ""
        if user_favorite_company:
            user_favorite_company = user_favorite_company.company_name
        return render(request, 'app_main/survey.html', {'user_favorite_company': user_favorite_company})

    def post(self, request):
        company_name = request.POST.get('company')
        justification = request.POST.get('justification')
        user_id = request.user.pk
        FavoriteCruiseCompany.objects.create(
            user_id=user_id,
            company_name=company_name,
            justification=justification,
        )
        return redirect('app_main:survey')
