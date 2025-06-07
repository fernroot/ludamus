from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    class Meta:
        db_table = "crowd_user"


class Auth0User(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vendor = models.CharField(max_length=255)
    external_id = models.CharField(max_length=255)

    class Meta:
        db_table = "crowd_auth0_user"

    def __str__(self) -> str:
        return f"{self.vendor}|{self.external_id}"
