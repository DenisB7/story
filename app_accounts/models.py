from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    When you will have new model which you will need to link with User model,
    please don't use standard User model for ForeignKey, since we modified it, take it from settings.py:

    from project_demo.settings import AUTH_USER_MODEL

    class AnotherModel(models.Model):
        user = models.ForeignKey(AUTH_USER_MODEL, ...)
    """
    COUNTRY_CHOICES = (
        ('us', 'USA'),
        ('jp', 'Japan'),
        ('uk', 'United Kingdom'),
        ('sz', 'SWITZERLAND'),
    )
    country = models.CharField(max_length=5, choices=COUNTRY_CHOICES, blank=True)

    def __str__(self):
        return self.username
