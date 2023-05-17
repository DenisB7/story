from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import UserPassesTestMixin

from app_accounts.forms import UserCreationFormCustom


class MainView(View):

    def get(self, request):
        return render(request, 'main.html', {'username': request.user.username})


class RegisterView(UserPassesTestMixin, CreateView):
    form_class = UserCreationFormCustom
    template_name = "app_accounts/register.html"
    success_url = reverse_lazy('app_accounts:main')

    def test_func(self):
        return self.request.user.is_anonymous

    def handle_no_permission(self):
        return redirect('app_accounts:main')
