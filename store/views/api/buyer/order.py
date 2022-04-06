from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED

from core.permissions import IsBuyerUser
from store.serializers.buyer.order import OrderSerializer
from store.models import Order


class OrderApiView(APIView):
    permission_classes = [IsAuthenticated, IsBuyerUser]

    def get(self, request, *args, **kwargs):
        order = Order.objects.filter(buyer=request.user.buyer)
        serializer = OrderSerializer(order, many=True, context={"request": request})
        return Response(serializer.data, status=HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = OrderSerializer(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=HTTP_201_CREATED)
