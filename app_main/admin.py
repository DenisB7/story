from django.contrib import admin

from app_main.models import CompanyCruise


@admin.register(CompanyCruise)
class CompanyCruiseAdmin(admin.ModelAdmin):
    list_display = ('name', 'user')
    list_filter = ('name', 'user')
