from django.db import models

from core.models import BaseModel, Buyer
from store.models import Product, Variant


class Cart(BaseModel):
    class Meta:
        db_table = "carts"
        verbose_name = "Cart"
        verbose_name_plural = "Carts"

    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)

    def __str__(self):
        return self.buyer.user.username
