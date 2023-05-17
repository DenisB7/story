from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    COUNTRY_CHOICES = (
        ('us', 'USA'),
        ('jp', 'Japan'),
        ('uk', 'United Kingdom'),
        ('sz', 'SWITZERLAND'),
    )
    country = models.CharField(max_length=5, choices=COUNTRY_CHOICES, blank=True)

    def __str__(self):
        return self.username
