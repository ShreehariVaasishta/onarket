from django.db import models

from core.models import BaseModel, Seller
from store.models import Order, Product, VariantOption


class OrderStatuses(models.TextChoices):
    PENDING = "pending"
    DECLINED = "declined"
    ACCEPTED = "accepted"
    DISPATCHED = "dispatched"
    DELIVERED = "delivered"


class PaymentModes(models.TextChoices):
    CASH_ON_DELIVERY = "cash_on_delivery"
    ONLINE = "online"


class OrderProduct(BaseModel):
    class Meta:
        db_table = "order_products"
        verbose_name = "Order Product"
        verbose_name_plural = "Order Products"

    seller = models.ForeignKey(
        Seller,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_name = models.CharField(
        max_length=250,
        null=False,
        blank=False,
    )
    product = models.ForeignKey(
        Product, on_delete=models.SET_NULL, null=True, blank=True
    )
    product_variant = models.ForeignKey(
        VariantOption,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False,
        blank=False,
    )
    quantity = models.PositiveIntegerField(default=1, null=False, blank=False)

    @property
    def total_price(self):
        return self.orderproducts_set.all().aggregate(models.Sum("price"))
