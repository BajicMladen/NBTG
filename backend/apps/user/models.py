from common.mixins.model import TimestampedModelMixin
from django.contrib.auth.models import AbstractUser
from django.db import models

from .managers import UserManager


class User(TimestampedModelMixin, AbstractUser):
    email = models.EmailField("Email address", unique=True)
    objects = UserManager()

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "users"
