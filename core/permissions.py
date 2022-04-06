from rest_framework.permissions import BasePermission


class IsBuyerUser(BasePermission):
    def has_permission(self, request, view):
        return hasattr(request.user, "buyer")

    def has_object_permission(self, request, view, obj):
        return hasattr(request.user, "buyer")


class IsSellerUser(BasePermission):
    def has_permission(self, request, view):
        return hasattr(request.user, "seller")

    def has_object_permission(self, request, view, obj):
        return (
            obj.seller == request.user.seller
            if hasattr(request.user, "seller")
            else False
        )
