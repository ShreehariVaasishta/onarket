from django.db import transaction

from rest_framework.serializers import SerializerMethodField

from store.models import Product, Category, ProductCategory
from .list import ProductListSerializer
from store.serializers.variant import VariantSerializer


class ProductDetailSerializer(ProductListSerializer):
    variants = SerializerMethodField()

    class Meta:
        model = Product
        fields = ProductListSerializer.Meta.fields + ["variants"]

    def get_variants(self, product: Product):
        variants = product.variant_set.all()
        variants_serializer = VariantSerializer(variants, many=True)
        return variants_serializer.data

    def create(self, validated_data):
        with transaction.atomic():
            categories = self._request.data.get("categories")
            product = Product.objects.create(
                name=validated_data.get("name"), seller=self._request.user.seller
            )
            _product_categories = []
            for category in categories:
                _category = Category.objects.create(
                    name=category["name"], seller=self._request.user.seller
                )
                _product_categories.append(
                    ProductCategory(
                        product=product,
                        category=_category,
                    )
                )
            if _product_categories:
                ProductCategory.objects.bulk_create(_product_categories)
        return product
