
from django import forms
from booking.models import Booking


class CreateBookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['property', 'check_in', 'check_out', 'guests']
        exclude = ['user', 'status', 'total_price', 'created_at', 'updated_at']
        widgets = {
            'property': forms.Select(attrs={'class': 'form-control'}),
            'check_in': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'check_out': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'guests': forms.NumberInput(attrs={'min': 1, 'class': 'form-control'}),
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
