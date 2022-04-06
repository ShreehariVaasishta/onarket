from django.db import IntegrityError
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_201_CREATED

from core.models import Seller
from core.serializers import SellerSerializer
from core.permissions import IsSellerUser


class SellerAPIView(CreateAPIView, RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated, IsSellerUser]
    serializer_class = SellerSerializer

    def get_queryset(self):
        return Seller.objects.get(user=self.request.user)

    def get_object(self):
        return self.get_queryset()

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAuthenticated()]
        return super().get_permissions()

    def post(self, request, *args, **kwargs):
        try:
            seller = Seller.objects.create(
                user=request.user,
                store_name=request.data.get("store_name"),
                store_address=request.data.get("store_address"),
                store_postal_code=request.data.get("store_postal_code"),
            )
            serializer = SellerSerializer(seller)
            return Response(serializer.data, status=HTTP_201_CREATED)
        except IntegrityError:
            return Response(
                {"message": "Store already exists"}, status=HTTP_400_BAD_REQUEST
            )

    def get(self, request, *args, **kwargs):
        serializer = SellerSerializer(request.user.seller)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        serializer = SellerSerializer(
            request.user.seller, data=request.data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
