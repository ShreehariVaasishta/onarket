import logging

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.authtoken.models import Token

from core.models import User
from core.serializers import UserSerializer

# from core.utils import validate_user_otp


class UserLoginApiView(APIView):
    def post(self, request, *args, **kwargs):
        """Login user
        :param phone: phone number
        :param otp: Random 4 digit number. Complete OTP functionality is not added.
        """
        try:
            user = User.objects.get(phone=request.data.get("phone"))
            # is_otp_valid = validate_user_otp(user, request.data.get("otp"))
            # if not is_otp_valid:
            #     return Response({"error": "Invalid OTP"}, status=HTTP_400_BAD_REQUEST)
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=HTTP_200_OK)
        except User.DoesNotExist as ude:
            logging.error(ude)
            return Response(
                {"error": "User does not exist, kindly register"},
                status=HTTP_400_BAD_REQUEST,
            )
