from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View

from app_accounts.forms import UserCreationFormCustom
from django.views.generic.edit import CreateView

class MainView(View):

    def get(self, request):
        return render(request, 'main.html', {'username': request.user.username})


class RegisterView(CreateView):
    form_class = UserCreationFormCustom
    template_name = "app_accounts/register.html"
    success_url = reverse_lazy('app_accounts:main')
