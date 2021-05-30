from typing import AbstractSet
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    USER_CUSTOMER = "customer"
    USER_SELLER = "seller"
    USER_ADMIN = "admin"
    USER_TYPES = (
        (USER_CUSTOMER, "Customer"),
        (USER_SELLER, "Seller"),
    )
    # for define model
    USER_TYPE_CHOICES = (
        (USER_CUSTOMER, "Customer"),
        (USER_SELLER, "Seller"),
        (USER_ADMIN, "Admin"),
    )

    user_type = models.CharField(choices=USER_TYPE_CHOICES, max_length=10, blank=True)
    address = models.CharField(max_length=80, blank=True)
    restaurant_id = models.IntegerField(default=-1)# set default restaurant as none