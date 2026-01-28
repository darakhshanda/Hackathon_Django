from django.db import models

# Create your models here.


class Availability(models.Model):
    availability_id = models.AutoField(primary_key=True)
    property_id = models.ForeignKey(
        'property.Property', on_delete=models.CASCADE)
    date = models.DateField()
    is_available = models.BooleanField(default=True)
    # for special pricing on specific dates
    price_override = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'availability'
        verbose_name = 'Availability'
        verbose_name_plural = 'Availabilities'
        constraints = [
            models.UniqueConstraint(
                fields=['property_id', 'date'], name='unique_property_date')
        ]

    def __str__(self):
        return f"Availability for Property {self.property_id} on {self.date}: {'Available' if self.is_available else 'Not Available'}"

    def mark_unavailable(self):
        self.is_available = False
        self.save()

    def mark_available(self):
        self.is_available = True
        self.save()

    def set_price_override(self, new_price):
        self.price_override = new_price
        self.save()

    def clear_price_override(self):
        self.price_override = None
        self.save()
