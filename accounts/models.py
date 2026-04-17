from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    organization = models.ForeignKey(
        'organizations.Organization',
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name='users',
    )
    is_org_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.username
