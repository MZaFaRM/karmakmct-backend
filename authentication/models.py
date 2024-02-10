from uuid import uuid4
from . import validation as val

from django.db import models

# fmt: off
class CampusAmbassador(models.Model):
    id = models.UUIDField(max_length=255, default=uuid4, primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255, unique=True, validators=[val.validate_gmail])
    password = models.CharField(max_length=255)
    college = models.CharField(max_length=50)
    phone = models.CharField(max_length=10, unique=True, validators=[val.validate_number])
    referral_code = models.CharField(max_length=6, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "campus_ambassador"
