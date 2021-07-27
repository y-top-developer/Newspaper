from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    company = models.CharField(max_length=40)