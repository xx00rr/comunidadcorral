from django.contrib import admin
from .models import Unit


@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ['identifier', 'unit_type', 'status', 'organization', 'floor', 'area_m2']
    list_filter = ['organization', 'unit_type', 'status']
    search_fields = ['identifier']
