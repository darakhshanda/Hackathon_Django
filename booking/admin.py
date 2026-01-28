from django.contrib import admin
from booking import models
from .models import Booking

@admin.register(models.Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['user', 'property', 'check_in', 'check_out', 'guests', 'status', 'total_price', 'created_at']
    list_filter = ['status', 'check_in', 'check_out', 'created_at']
    search_fields = ['user__username', 'property__name', 'status']
    
    # Add actions for quick approval
    actions = ['approve_bookings', 'cancel_bookings']
    
    def approve_bookings(self, request, queryset):
        """Approve selected bookings"""
        updated = queryset.update(status='confirmed')
        self.message_user(request, f'{updated} bookings were approved.')
    approve_bookings.short_description = "Approve selected bookings"
    
    def cancel_bookings(self, request, queryset):
        """Cancel selected bookings"""
        updated = queryset.update(status='cancelled')
        self.message_user(request, f'{updated} bookings were cancelled.')
    cancel_bookings.short_description = "Cancel selected bookings"