from django.contrib import admin

from app_main.models import FavoriteCruiseCompany


@admin.register(FavoriteCruiseCompany)
class FavoriteCruiseCompanyAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'user', 'justification')
    list_filter = ('company_name', 'user')
