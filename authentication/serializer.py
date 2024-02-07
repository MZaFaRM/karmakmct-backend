from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from rest_framework import serializers

from authentication.validation import clean_gmail

from .models import User


class UserAuthenticationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def to_representation(self, instance):
        value = super().to_representation(instance)
        value["email"] = f"{value['email']}@gmail.com"
        return value

    def validate_email(self, email):
        email = clean_gmail(email)
        if User.objects.filter(email=email).exists():
            raise ValidationError("user with this email already exists")
        return email

    def create(self, validated_data):
        validated_data.update(
            {
                "password": make_password(validated_data.get("password").strip()),
                "email": validated_data.get("email"),
                "name": validated_data.get("name").strip(),
                "college": validated_data.get("college", "").strip(),
            }
        )

        return super().create(validated_data)

    class Meta:
        model = User
        fields = ["name", "email", "password", "college", "phone"]
