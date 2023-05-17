from project_demo.settings import AUTH_USER_MODEL
from django.db import models


class CompanyCruise(models.Model):
    NAMES_CHOICES = (
        ('storylines', 'storylines'),
    )
    name = models.CharField(max_length=20, choices=NAMES_CHOICES)
    justification = models.TextField()
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="company_cruise")

    def __str__(self):
        return f"{self.user.username}"
