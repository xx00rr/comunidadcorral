from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ['username', 'email', 'organization', 'is_org_admin', 'is_staff']
    list_filter = ['organization', 'is_org_admin', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        ('Organización', {'fields': ('organization', 'is_org_admin')}),
    )
