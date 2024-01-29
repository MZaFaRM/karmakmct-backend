from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from .models import User


class UserAuthenticationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def validate_phone(self, phone):
        if len(phone) != 10 or not phone.isdigit():
            raise serializers.ValidationError("Invalid phone number")
        return phone

    def create(self, validated_data):
        validated_data.update(
            {
                "password": make_password(validated_data.get("password", "").strip()),
                "email": validated_data.get("email", "").lower().strip(),
                "name": validated_data.get("name", "").strip(),
                "college": validated_data.get("college", "").strip(),
            }
        )

        return super().create(validated_data)

    class Meta:
        model = User
        fields = ["name", "email", "password", "college", "phone"]
