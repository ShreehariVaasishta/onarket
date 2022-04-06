from django.urls import reverse
from rest_framework.serializers import SerializerMethodField

from core.models import User
from core.serializers import UserSerializer


class UserProfileSerializer(UserSerializer):
    seller_url = SerializerMethodField()
    # buyer_url = BuyerSerializer(source="buyer")

    class Meta:
        model = UserSerializer.Meta.model
        fields = UserSerializer.Meta.fields + [
            "seller_url",
        ]
        read_only_fields = [
            "seller_url",
        ]

    def get_seller_url(self, user: User):
        return self.context["request"].build_absolute_uri(reverse("core:api:seller"))
