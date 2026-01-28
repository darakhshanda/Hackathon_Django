from django.contrib import admin
from django.contrib.auth.models import User
from userprofile.models import UserProfile

# Register your models here.


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'first_name', 'last_name',
                    'email', 'phone_number', 'is_active']
    list_filter = ['is_active', 'created_at']
    search_fields = ['user.username', 'email']
