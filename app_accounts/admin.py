from django.contrib import admin

from app_accounts.models import User


@admin.register(User)
class UserExtendedAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'country')
    list_filter = ('username', 'email', 'country')
    list_editable = ('country', )
