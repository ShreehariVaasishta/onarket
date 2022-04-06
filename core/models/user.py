from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinLengthValidator


class User(AbstractUser):
    class Meta:
        db_table = "users"
        verbose_name = "User"
        verbose_name_plural = "Users"

    phone = models.CharField(
        max_length=12,
        unique=True,
        null=False,
        blank=False,
        validators=[MinLengthValidator(4)],
    )
    profile_image = models.ImageField(
        upload_to="profile_images",
        null=True,
        blank=True,
    )
