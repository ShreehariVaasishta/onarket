from django.db import transaction
from functools import cached_property
from rest_framework.serializers import ModelSerializer, SerializerMethodField

from store.models import Cart, CartProduct, Product
from .product.list import BuyerProductListSerializer


class BuyerCart(ModelSerializer):
    products = SerializerMethodField()

    class Meta:
        model = Cart
        fields = ["id", "buyer", "products"]
        read_only_fields = ["id", "buyer"]

    @cached_property
    def _request(self):
        return self.context["request"]

    def get_products(self, cart):
        cart_products = Product.objects.filter(cartproduct__cart=cart)
        return BuyerProductListSerializer(
            cart_products, many=True, context=self.context
        ).data

    def create(self, validated_data):
        with transaction.atomic():
            cart, _ = Cart.objects.get_or_create(buyer=self._request.user.buyer)
            if cart_products := self._request.data.get("products"):
                _cart_products = [
                    CartProduct(
                        cart=cart,
                        product_id=product.get("product_id"),
                        variant_id=product.get("variant_id"),
                        quantity=product.get("quantity"),
                    )
                    for product in cart_products
                ]
                CartProduct.objects.bulk_create(_cart_products)

            return cart
