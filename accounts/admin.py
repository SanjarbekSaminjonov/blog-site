from django.contrib import admin
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.admin import UserAdmin

# Register your models here.


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = [
        'username',
        'first_name',
        'email',
        'mobile',
        'region',
        'is_staff'
    ]
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Additional information',
            {
                'fields': (
                    'mobile',
                    'region'
                )
            }
        )
    )


admin.site.register(CustomUser, CustomUserAdmin)
