from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated

from store.models import Product
from store.serializers.buyer.product.list import BuyerProductListSerializer
from store.serializers.buyer.product.detail import BuyerProductDetailSerializer
from core.permissions import IsBuyerUser


class BuyerProductViewSet(ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated, IsBuyerUser]
    queryset = Product.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return BuyerProductListSerializer
        return BuyerProductDetailSerializer
