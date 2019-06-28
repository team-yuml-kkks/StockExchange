from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class UserAdmin(auth_admin.UserAdmin):
    """
    Override user admin to display and modified data
    in new fields:
      -account_number,
      -bank_name,
      -address,
      -city_code.
    """
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields':(
            'first_name',
            'last_name',
            'account_number',
            'bank_name',
            'address',
            'city_code'
        )}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    list_display = (
        'email',
        'first_name',
        'last_name',
        'account_number',
        'bank_name',
        'address',
        'city_code',
        'is_superuser',
    )

admin.site.register(User, UserAdmin)