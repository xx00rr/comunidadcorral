from django.contrib import admin
from .models import Organization


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'contact_email', 'contact_phone', 'created_at']
    prepopulated_fields = {'slug': ('name',)}
