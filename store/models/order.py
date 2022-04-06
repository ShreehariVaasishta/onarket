from django.db import models

from core.models import BaseModel, Buyer


class OrderStatuses(models.TextChoices):
    PENDING = "pending"
    DECLINED = "declined"
    ACCEPTED = "accepted"
    DISPATCHED = "dispatched"
    DELIVERED = "delivered"


class PaymentModes(models.TextChoices):
    CASH_ON_DELIVERY = "cash_on_delivery"
    ONLINE = "online"


class Order(BaseModel):
    class Meta:
        db_table = "orders"
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=20,
        choices=OrderStatuses.choices,
        default=OrderStatuses.PENDING,
    )
    payment_info = models.TextField(blank=True, null=True)
    payment_mode = models.CharField(choices=PaymentModes.choices, max_length=20)

    @property
    def total_price(self):
        return self.orderproducts_set.all().aggregate(models.Sum("price"))
