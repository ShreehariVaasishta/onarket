from store.models import Product
from store.serializers.seller.product.detail import ProductDetailSerializer
from .list import BuyerProductListSerializer


class BuyerProductDetailSerializer(ProductDetailSerializer, BuyerProductListSerializer):
    class Meta:
        model = Product
        fields = BuyerProductListSerializer.Meta.fields

    def create(self, validated_data):
        raise "Buyers cannot create products"
