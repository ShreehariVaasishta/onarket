from django.db import models

from core.models import BaseModel
from store.models import Product


class Variant(BaseModel):
    class Meta:
        db_table = "variants"
        verbose_name = "Variant"
        verbose_name_plural = "Variants"

    name = models.CharField(max_length=250, null=False, blank=False)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, null=False, blank=False
    )
