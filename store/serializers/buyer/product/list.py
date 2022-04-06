from django.db import transaction
from django.urls import reverse

from functools import cached_property
from rest_framework.serializers import ModelSerializer, SerializerMethodField

from store.models import Product
from store.serializers.seller.product.list import ProductListSerializer


class BuyerProductListSerializer(ProductListSerializer):
    class Meta:
        model = ProductListSerializer.Meta.model
        fields = ProductListSerializer.Meta.fields
        read_only_fields = ProductListSerializer.Meta.read_only_fields

    def get_url(self, product: Product):
        return self._request.build_absolute_uri(
            reverse("store:api:buyer-products-detail", kwargs={"pk": product.pk})
        )
