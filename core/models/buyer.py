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
    store_name = models.CharField(max_length=150, null=False, blank=False)
    store_address = models.CharField(max_length=250, null=False, blank=False)
    store_postal_code = models.PositiveIntegerField(null=False, blank=False)

    def __str__(self) -> str:
        return f"{self.user.username} {self.store_name}"
