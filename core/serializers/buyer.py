from rest_framework.serializers import ModelSerializer

from core.models import Buyer


class BuyerSerializer(ModelSerializer):
    class Meta:
        model = Buyer
        fields = [
            "id",
            "user",
        ]
        read_only_fields = ["user"]
