from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from account.models import User


# Register your models here.
class UserModelAdmin(UserAdmin):
    model = User
    # The fields to be used in displaying the User Model.
    # These override the definition on the base UserModelAdmin.
    # that reference specific fields on auth.User.
    list_display = [
        "id",
        "email",
        "name",
        "is_active",
        "is_superuser",
        "is_staff",
        "is_customer",
        "is_seller",
    ]
    list_filter = ["is_superuser"]
    fieldsets = [
        ("User Credentials", {"fields": ["email", "password"]}),
        ("Personal Information", {"fields": ["name", "city"]}),
        (
            "Permissions",
            {
                "fields": [
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "is_customer",
                    "is_seller",
                ]
            },
        ),
    ]  # 'groups', 'user_permissions'
    # add_fieldsets is not a standard ModelAdmin attribute.
    # Overrides get_fieldsets to use this attribute when creating a user.
    # add_fieldsets is a list of tuples. Each tuple represents
    # section in the Add User form.

    add_fieldsets = [
        (
            # It is the title of the section. Setting this to None leaves the section title blank.
            None,
            {
                # Its a css class to make full width admin layout
                "classes": ["wide"],
                # This fields will appear in admin panel add user form
                "fields": ["email", "password1", "password2"],
            },
        ),
    ]

    search_fields = ["email"]
    ordering = ["email", "id"]
    filter_horizontal = []  # "groups", "user_permissions"


# Now register the new UserModelAdmin
admin.site.register(User, UserModelAdmin)
