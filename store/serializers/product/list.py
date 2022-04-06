from django.db import transaction
from django.urls import reverse

from functools import cached_property
from rest_framework.serializers import ModelSerializer, SerializerMethodField

from store.models import Product, Category, ProductCategory
from store.serializers.category import CategorySerializer


class ProductListSerializer(ModelSerializer):
    categories = SerializerMethodField()
    url = SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            "id",
            "url",
            "name",
            "categories",
        ]
        read_only_fields = [
            "categories",
        ]

    @cached_property
    def _request(self):
        return self.context["request"]

    def get_categories(self, product: Product):
        return CategorySerializer(
            Category.objects.filter(productcategory__product=product), many=True
        ).data

    def get_url(self, product: Product):
        return self._request.build_absolute_uri(
            reverse("store:api:products-detail", kwargs={"pk": product.id})
        )
