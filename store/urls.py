from django.urls import path, include
from rest_framework import routers
from rest_framework_nested import routers as nested_routers

from store.views.api.seller import (
    SellerProductViewSet,
    SellerProductVariantViewSet,
    SellerOrdersApiView,
)
from store.views.api.buyer import BuyerProductViewSet, BuyerCartApiView, OrderApiView


app_name = "store"

# Seller Routers
seller_router = routers.DefaultRouter()
seller_router.register(
    r"products",
    SellerProductViewSet,
    basename="products",
)
nested_router = nested_routers.NestedDefaultRouter(
    seller_router,
    r"products",
    lookup="product",
)
nested_router.register(
    "variants",
    SellerProductVariantViewSet,
    basename="variant",
)

# Seller Routers
buyer_router = routers.DefaultRouter()
buyer_router.register(
    r"products",
    BuyerProductViewSet,
    basename="buyer-products",
)


urlpatterns = [
    path(
        "api/",
        include(
            (
                [
                    path(
                        "seller/",
                        include(seller_router.urls + nested_router.urls),
                        name="seller",
                    ),
                    path(
                        "seller/orders",
                        SellerOrdersApiView.as_view(),
                        name="sellers-orders",
                    ),
                    path(
                        "buyer/",
                        include(buyer_router.urls),
                        name="buyer",
                    ),
                    path(
                        "buyer/cart/",
                        BuyerCartApiView.as_view(),
                        name="buyer-cart",
                    ),
                    path(
                        "buyer/order/",
                        OrderApiView.as_view(),
                        name="order",
                    ),
                    # TODO: include order and cart url paths into buyer/
                ],
                app_name,
            ),
            namespace="api",
        ),
    ),
]
