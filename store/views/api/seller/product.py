from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from store.models import Product, ProductCategory, Variant, VariantOption
from store.serializers import ProductListSerializer, ProductDetailSerializer
from core.permissions import IsSellerUser


class SellerProductViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, IsSellerUser]

    def get_queryset(self):
        return Product.objects.filter(seller=self.request.user.seller)

    def get_serializer_class(self):
        if self.action == "list":
            return ProductListSerializer
        return ProductDetailSerializer
