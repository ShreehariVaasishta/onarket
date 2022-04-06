from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from core.permissions import IsSellerUser
from store.models import OrderProduct
from store.serializers.buyer.order_product import OrderProductSerializer


class SellerOrdersApiView(APIView):
    # TODO: Patch to update the statuses of the respective orders
    permission_classes = [IsAuthenticated, IsSellerUser]

    def get(self, request, *args, **kwargs):
        order_products = OrderProduct.objects.filter(seller=request.user.seller)
        serializer = OrderProductSerializer(order_products, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
