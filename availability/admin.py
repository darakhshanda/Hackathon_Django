from django.contrib import admin
from availability import models

# Register your models here.


@admin.register(models.Availability)
class AvailabilityAdmin(admin.ModelAdmin):
    list_display = ['property_id', 'date', 'is_available', 'created_at']
    list_filter = ['is_available', 'date', 'created_at']
    search_fields = ['property_id__name']
