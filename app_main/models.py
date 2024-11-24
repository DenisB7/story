from project_demo.settings import AUTH_USER_MODEL
from django.db import models


def get_order_number(instance):
    return instance.pk


class FavoriteCruiseCompany(models.Model):
    NAMES_CHOICES = (
        ('storylines', 'storylines'),
    )
    company_name = models.CharField(max_length=20, choices=NAMES_CHOICES)
    justification = models.TextField()
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="company_cruise")
    order_number = models.PositiveBigIntegerField(default=get_order_number)

    def __str__(self):
        return f"USER {self.user.username} FAVORITE CRUISE COMPANY {self.company_name}"
