from django.core.exceptions import ValidationError
from django.core.validators import validate_email


def validate_gmail(value):
    """
    Custom validator to ensure email addresses belong to a Google domain.
    """
    value = value.strip().lower()
    if not value.endswith("@gmail.com"):
        raise ValidationError(
            "Email address must belong to a Gmail domain (gmail.com)."
        )


def clean_gmail(gmail):
    return gmail.lower().strip().replace("@gmail.com", "").replace(".", "")


def validate_number(value):
    """
    Custom validator to ensure mobile number is Indian.
    """
    if len(value) != 10 or not value.isdigit():
        raise ValidationError("Invalid phone number")
