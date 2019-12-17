from django.db import models

# Create your models here.

import uuid

from django.contrib.auth.models import AbstractBaseUser, UserManager

class AppUser(AbstractBaseUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=80)
    email = models.EmailField(null=True, blank=True)

    objects = UserManager()
    USERNAME_FIELD = 'username'


