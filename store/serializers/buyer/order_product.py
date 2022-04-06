from rest_framework.serializers import ModelSerializer
from store.models import OrderProduct


class OrderProductSerializer(ModelSerializer):
    class Meta:
        model = OrderProduct
        fields = ["id", "order", "product_name", "product", "quantity", "price"]
