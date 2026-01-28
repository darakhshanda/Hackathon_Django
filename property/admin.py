from pyexpat import model
from django.contrib import admin
from django.contrib.auth.models import User
from property import models


# Register your models here.
@admin.register(models.Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'address', 'max_guests',
                    'price_per_night', 'created_by', 'category', 'created_at']
    list_filter = ['category', 'created_at']
    search_fields = ['name', 'location', 'address', 'category']
