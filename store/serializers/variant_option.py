from rest_framework.serializers import ModelSerializer, SerializerMethodField

from store.models import VariantOption


class VariantOptionSerializer(ModelSerializer):
    class Meta:
        model = VariantOption
        fields = ["description", "price", "quantity"]
