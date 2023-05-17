from django.contrib import admin

from app_accounts.models import User


@admin.register(User)
class UserExtendedAdmin(admin.ModelAdmin):
    pass
