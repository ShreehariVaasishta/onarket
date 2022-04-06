from django.contrib import admin
from core.models import User, Buyer, Seller

# Register your models here.
admin.site.register(User)


@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    raw_id_fields = ("user",)


@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    raw_id_fields = ("user",)
