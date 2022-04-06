from django.db import models

from core.models import BaseModel
from store.models import Category, Product


class ProductCategory(BaseModel):
    class Meta:
        db_table = "product_categories"
        verbose_name = "Product Category"
        verbose_name_plural = "Product Categories"

    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, null=False, blank=False
    )
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=False, blank=False
    )
