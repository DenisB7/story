from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass

    def __str__(self):
        return f"USERNAME: {self.username} EMAIL: {self.email}"
