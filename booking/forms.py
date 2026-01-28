
from booking.models import Booking
from property import models
from availability import models
from userprofile import forms
from django import forms


class CreateBookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['property.Property', 'check_in',
                  'check_out', 'guests', 'package']
        exclude = ['user', 'status', 'total_price', 'created_at', 'updated_at']
        widgets = {

            'property': forms.TextInput(attrs={'class': 'form-control'}),
            'check_in': forms.DateInput(attrs={'type': 'date'}),
            'check_out': forms.DateInput(attrs={'type': 'date'}),
            'guests': forms.NumberInput(attrs={'min': 1}),

        }

    def clean(self):
        cleaned_data = super().clean()
        check_in = cleaned_data.get('check_in')
        check_out = cleaned_data.get('check_out')

        if check_in and check_out:
            if check_in >= check_out:
                raise forms.ValidationError(
                    "Check-out date must be after check-in date.")
        if check_in and check_in < models.Availability.today_date():
            raise forms.ValidationError(
                "Check-in date cannot be in the past.")
        return cleaned_data
