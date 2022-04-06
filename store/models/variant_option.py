from django.db import models

from core.models import BaseModel
from store.models import Variant


class VariantOption(BaseModel):
    class Meta:
        db_table = "variant_options"
        verbose_name = "Variant Option"
        verbose_name_plural = "Variants Options"

    variant = models.ForeignKey(
        Variant, on_delete=models.CASCADE, null=False, blank=False
    )
    description = models.CharField(max_length=250, null=True, blank=True)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, blank=False
    )
    quantity = models.PositiveIntegerField(null=False, blank=False)
