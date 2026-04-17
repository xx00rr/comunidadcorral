from django.contrib import admin
from .models import Resident


@admin.register(Resident)
class ResidentAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'unit', 'role', 'status', 'phone', 'email']
    list_filter = ['unit__organization', 'role', 'status']
    search_fields = ['first_name', 'last_name', 'identification']
