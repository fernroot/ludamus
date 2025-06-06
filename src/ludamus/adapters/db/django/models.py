from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Auth0User(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vendor = models.CharField(max_length=255)
    external_id = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.vendor}|{self.external_id}"
