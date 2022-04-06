from django.db import IntegrityError
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_201_CREATED

from core.models import Buyer
from core.serializers import BuyerSerializer
from core.permissions import IsBuyerUser


class BuyerAPIView(CreateAPIView, RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated, IsBuyerUser]
    serializer_class = BuyerSerializer

    def get_queryset(self):
        return Buyer.objects.get(user=self.request.user)

    def get_object(self):
        return self.get_queryset()

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAuthenticated()]
        return super().get_permissions()

    def post(self, request, *args, **kwargs):
        try:
            buyer = Buyer.objects.create(user=request.user)
            serializer = BuyerSerializer(buyer)
            return Response(serializer.data, status=HTTP_201_CREATED)
        except IntegrityError:
            return Response(
                {"message": "Buyer already exists"}, status=HTTP_400_BAD_REQUEST
            )

    def get(self, request, *args, **kwargs):
        serializer = BuyerSerializer(request.user.Buyer)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        serializer = BuyerSerializer(
            request.user.Buyer, data=request.data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
