from django.urls import path, include
from core.views.api import (
    UserRegisterApiView,
    UserLoginApiView,
    BuyerAPIView,
    SellerAPIView,
    UserProfileAPIView,
)

app_name = "core"

urlpatterns = [
    path(
        "api/",
        include(
            (
                (
                    [
                        path(
                            "auth/",
                            include(
                                [
                                    path(
                                        "register/",
                                        UserRegisterApiView.as_view(),
                                        name="register",
                                    ),
                                    path(
                                        "login/",
                                        UserLoginApiView.as_view(),
                                        name="login",
                                    ),
                                ]
                            ),
                        ),
                        path(
                            "user/",
                            UserProfileAPIView.as_view(),
                            name="user-profile",
                        ),
                        path(
                            "buyer/",
                            BuyerAPIView.as_view(),
                            name="buyer",
                        ),
                        path(
                            "seller/",
                            SellerAPIView.as_view(),
                            name="seller",
                        ),
                    ]
                ),
                "core",
            ),
            namespace="api",
        ),
    ),
]
