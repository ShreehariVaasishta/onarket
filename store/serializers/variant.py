from django.db import transaction
from rest_framework.serializers import ModelSerializer, SerializerMethodField

from store.models import Variant, VariantOption
from store.serializers.variant_option import VariantOptionSerializer


class VariantSerializer(ModelSerializer):
    variant_options = SerializerMethodField()

    class Meta:
        model = Variant
        fields = ["id", "product", "name", "variant_options"]
        read_only_fields = ["id", "product"]

    def get_variant_options(self, variant: Variant):
        variant_options = variant.variantoption_set.all()
        variant_options_serializer = VariantOptionSerializer(variant_options, many=True)
        return variant_options_serializer.data

    def create(self, validated_data):
        with transaction.atomic():
            variant = Variant.objects.create(
                name=validated_data.get("name"),
                product_id=self.context["view"].kwargs.get("product_pk"),
            )
            if variant_options := self.context["request"].data.get("variant_options"):
                _variant_options = [
                    VariantOption(
                        variant=variant,
                        description=variant_option.get("description"),
                        price=variant_option.get("price"),
                        quantity=variant_option.get("quantity"),
                    )
                    for variant_option in variant_options
                ]
                VariantOption.objects.bulk_create(_variant_options)
        return variant
