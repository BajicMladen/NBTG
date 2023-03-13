from common.mixins.model import TimestampedModelMixin
from django.contrib.auth.models import AbstractUser
from django.db import models

from .managers import UserManager


class User(TimestampedModelMixin, AbstractUser):
    username = None
    email = models.EmailField("Email address", unique=True)
    display_name = models.CharField(max_length=40, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "users"
