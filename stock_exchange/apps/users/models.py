from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Extending User model of field with stored
    extra information about user.
    """
    account_number = models.CharField(max_length=200, blank=True, null=True)
    bank_name = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=300, blank=True, null=True)
    city_code = models.CharField(max_length=7, blank=True, null=True)
