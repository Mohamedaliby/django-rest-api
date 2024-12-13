from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    city = models.CharField(max_length=25)
    center_name = models.CharField(max_length=25)

    def __str__(self):
        return self.first_name
