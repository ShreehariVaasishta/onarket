from django.db import models

from core.models import BaseModel
from store.models import Cart, Product, VariantOption


class CartProduct(BaseModel):
    class Meta:
        db_table = "cart_products"
        verbose_name = "Cart Product"
        verbose_name_plural = "Cart Products"

    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_variant = models.ForeignKey(VariantOption, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
