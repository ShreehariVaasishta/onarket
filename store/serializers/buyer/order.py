from django.db import transaction
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from rest_framework.exceptions import ValidationError
from store.models import Order, OrderProduct, Product, VariantOption
from .order_product import OrderProductSerializer


class OrderSerializer(ModelSerializer):
    ordered_products = SerializerMethodField()

    class Meta:
        model = Order
        fields = [
            "id",
            "buyer",
            "status",
            "payment_info",
            "payment_mode",
            "ordered_products",
        ]
        read_only_fields = ["id", "buyer", "ordered_products"]

    def get_ordered_products(self, order: Order):
        return OrderProductSerializer(order.orderproduct_set.all(), many=True).data

    def create(self, validated_data):
        # TODO: Move validation to serializer `validate()`
        # TODO: Break this method into smaller methods
        request = self.context["request"]
        with transaction.atomic():
            order = Order.objects.create(
                buyer=request.user.buyer,
                payment_mode=validated_data.get("payment_mode"),
            )
            ordered_products = request.data.pop("products")
            if not ordered_products:
                raise ValidationError(
                    {"detail": "An order should contain atleat one product"}
                )
            _ordered_products = []
            for product in ordered_products:
                _product = Product.objects.get(id=product["product_id"])
                try:
                    _variant_option: VariantOption = VariantOption.objects.get(
                        id=product["variant_id"]
                    )
                except VariantOption.DoesNotExist:
                    raise ValidationError(
                        {"detail": "Product variant does not exist anymore"}
                    )
                required_quantity = product.get("quantity", 0)
                if not required_quantity:
                    raise ValidationError(
                        {
                            "detail": "Quantity should be provided and should be greater than zero"
                        }
                    )

                total_variant_price = 0
                if required_quantity > _variant_option.quantity:
                    raise ValidationError(
                        {"detail": "Number of quantity exceeded the stock quantity"}
                    )
                _variant_option.quantity = _variant_option.quantity - required_quantity
                _variant_option.save()
                total_variant_price = _variant_option.price * required_quantity
                _ordered_products.append(
                    OrderProduct(
                        order=order,
                        seller=_product.seller,
                        product=_product,
                        product_variant_id=_variant_option.id,
                        price=total_variant_price,
                    )
                )
            OrderProduct.objects.bulk_create(_ordered_products)
        return order
