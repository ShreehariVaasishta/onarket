from django.db import models

from core.models import BaseModel, Seller


class Category(BaseModel):
    class Meta:
        db_table = "categories"
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=100, null=False, blank=False)
    seller = models.ForeignKey(
        Seller, on_delete=models.CASCADE, null=False, blank=False
    )

    def __str__(self) -> str:
        return self.name
