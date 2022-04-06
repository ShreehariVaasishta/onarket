from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action

from core.permissions import IsSellerUser
from store.models import Variant, VariantOption
from store.serializers import VariantSerializer


class SellerProductVariantViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, IsSellerUser]
    serializer_class = VariantSerializer

    def get_queryset(self):
        return Variant.objects.filter(product_id=self.request.GET.get("product_pk"))

    def perform_update(self, serializer):
        # TODO: Updating variants` info
        raise NotImplementedError
