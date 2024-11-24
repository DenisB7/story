from django.contrib.auth.forms import UserCreationForm

from app_accounts.models import User


class UserCreationFormCustom(UserCreationForm):

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2',
            'country',
        )
