from django.contrib.auth.models import AbstractUser
from django.db import models

class ClientUser(AbstractUser):
    is_manager = models.BooleanField(default=False)
    client_id = models.IntegerField()

    def __str__(self):
        return self.email
