from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from . import models

# Register your models here.
@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile", {
            'fields': (
                'user_type',
                'address'
                )
            },
        ),
    )
