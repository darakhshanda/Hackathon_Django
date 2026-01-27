# Register your models here.
from django.contrib import admin
from booking import models
from .models import Booking


@admin.register(models.Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['user', 'property', 'check_in',
                    'check_out', 'guests', 'status', 'total_price', 'created_at']
    list_filter = ['status', 'check_in', 'check_out', 'created_at']
    search_fields = ['user__username', 'property__name', 'status']
