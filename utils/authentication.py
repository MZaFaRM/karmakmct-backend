from rest_framework_simplejwt.tokens import RefreshToken
from authentication.models import CampusAmbassador


def generate_access_token(user):
    refresh = RefreshToken.for_user(user)
    access_token = str(refresh.access_token)
    return access_token

def generate_referral_code():
    referral_format = "CA24%d%d"
    
    last_created_user = CampusAmbassador.objects.order_by('-created_at').first()
    if not last_created_user:
        return referral_format % (0, 0)

    new_number = int(last_created_user.referral_code[4:]) + 1
    return referral_format % (new_number // 10, new_number % 10)
    
    