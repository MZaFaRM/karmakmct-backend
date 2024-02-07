from django.contrib.auth.hashers import check_password
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from authentication.models import User
from authentication.validation import clean_gmail
from utils.authentication import generate_access_token
from utils.response import CustomResponse

from .serializer import UserAuthenticationSerializer


class UserRegistrationView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]

    def post(self, request):
        serialized_data = UserAuthenticationSerializer(data=request.data)

        if not serialized_data.is_valid():
            return CustomResponse(
                message="User registration unsuccessful",
                errors=serialized_data.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )

        user = serialized_data.save()
        access_token = generate_access_token(user)

        return CustomResponse(
            message="User registered successfully",
            data={
                "user": UserAuthenticationSerializer(user).data,
                "access_token": access_token,
            },
            status=status.HTTP_201_CREATED,
        )


class UserLoginView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get("email", "")
        password = request.data.get("password", "")

        user = User.objects.filter(email=clean_gmail(email)).first()

        if user and check_password(password=password, encoded=user.password):
            # Authentication successful
            access_token = generate_access_token(user)

            return CustomResponse(
                message="User logged in successfully",
                data={
                    "user": UserAuthenticationSerializer(user).data,
                    "access_token": access_token,
                },
                status=status.HTTP_200_OK,
            )

        # Authentication failed
        return CustomResponse(
            message="Login unsuccessful",
            status=status.HTTP_401_UNAUTHORIZED,
            errors="Invalid credentials",
        )
