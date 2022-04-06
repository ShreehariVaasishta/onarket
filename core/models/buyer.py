from django.db import models

from core.models import BaseModel, User


class Buyer(BaseModel):
    class Meta:
        db_table = "buyers"
        verbose_name = "Buyer"
        verbose_name_plural = "Buyers"

    user = models.OneToOneField(
        User,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
    )

    def __str__(self) -> str:
        return f"{self.user.username} {self.store_name}"
