import imp
from django.db import models

from core.models import BaseModel, Seller


class Product(BaseModel):
    class Meta:
        db_table = "products"
        verbose_name = "Product"
        verbose_name_plural = "Products"

    name = models.CharField(max_length=250, null=False, blank=False)
    seller = models.ForeignKey(
        Seller, on_delete=models.CASCADE, null=False, blank=False
    )
