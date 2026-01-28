from django import forms
from booking.models import Booking
from datetime import date

class CreateBookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['check_in', 'check_out', 'guests']  # Remove 'property'
        widgets = {
            'check_in': forms.DateInput(
                attrs={
                    'type': 'date', 
                    'class': 'form-control',
                    'min': date.today().isoformat()
                }
            ),
            'check_out': forms.DateInput(
                attrs={
                    'type': 'date', 
                    'class': 'form-control',
                    'min': date.today().isoformat()
                }
            ),
            'guests': forms.NumberInput(
                attrs={
                    'min': 1, 
                    'class': 'form-control'
                }
            ),
        }
    
    def clean(self):
        cleaned_data = super().clean()
        check_in = cleaned_data.get('check_in')
        check_out = cleaned_data.get('check_out')

        if check_in and check_out:
            if check_in >= check_out:
                raise forms.ValidationError(
                    "Check-out date must be after check-in date."
                )
            if check_in < date.today():
                raise forms.ValidationError(
                    "Check-in date cannot be in the past."
                )
        return cleaned_data