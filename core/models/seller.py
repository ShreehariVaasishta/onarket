from django.db import models

from core.models import BaseModel, User


class Seller(BaseModel):
    """This model contains the seller's information along with some store details"""

    class Meta:
        db_table = "sellers"
        verbose_name = "Seller"
        verbose_name_plural = "Sellers"

    user = models.OneToOneField(User, null=False, blank=False, on_delete=models.CASCADE)
    store_name = models.CharField(max_length=150, null=False, blank=False)
    store_address = models.CharField(max_length=250, null=False, blank=False)
    store_postal_code = models.PositiveIntegerField(null=False, blank=False)

    def __str__(self) -> str:
        return f"{self.user.username} {self.store_name}"
