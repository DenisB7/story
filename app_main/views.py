from django.shortcuts import render
from django.views import View


class MainView(View):

    def get(self, request):
        return render(request, 'app_main/main.html', {'username': request.user.username})
