from rest_framework.serializers import ModelSerializer

from core.models import Seller


class SellerSerializer(ModelSerializer):
    class Meta:
        model = Seller
        fields = [
            "id",
            "user",
            "store_name",
            "store_address",
            "store_postal_code",
        ]
        read_only_fields = ["user"]
