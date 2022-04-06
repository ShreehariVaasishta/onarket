from core.models import User


def validate_user_otp(user: User, otp: int) -> bool:
    return UserOtp.objects.filter(user=user, otp=request.data.get("otp")).exists()
