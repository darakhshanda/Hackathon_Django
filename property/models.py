from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User


# Create your models here.


class Property(models.Model):
    CATEGORY_CHOICES = [
        ('apartment', 'Apartment'),
        ('house', 'House'),
        ('villa', 'Villa'),
        ('cabin', 'Cabin'),
        ('studio', 'Studio'),
    ]
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    max_guests = models.IntegerField()
    image_list = models.FileField(CloudinaryField('image'))
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='properties')
    category = models.CharField(
        max_length=50, choices=CATEGORY_CHOICES, default='apartment')
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'properties'
        verbose_name = 'Property'
        verbose_name_plural = 'Properties'
        ordering = ['-created_at']

    def is_available(self, check_in, check_out):
        """Check if property is available for given dates"""
        from booking.models import Booking

        conflicting_bookings = Booking.objects.filter(
            property=self,
            status__in=['confirmed', 'pending'],
            check_in__lt=check_out,      # Use the parameter, not Booking.check_out
            check_out__gt=check_in,      # Use the parameter, not Booking.check_in
        ).exists()

        return not conflicting_bookings
