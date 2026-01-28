from django import forms
import re

from availability import models
from .models import Property
from django.core.exceptions import ValidationError


class CreatePropertyForm(forms.ModelForm):
    """Form for creating a new property"""

    class Meta:
        model = Property
        fields = ['first_name', 'last_name', 'email', 'phome_number',]
        exclude = ['created_at', 'updated_at', 'is_active',]
        widgets = {
            'first_name': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Enter your full name'}),
            'last_name': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Enter your full name'}),
            'email': forms.EmailInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Enter your email address'}),
            'phome_number': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Enter your phone number'}),
        }

        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email Address',
            'phome_number': 'Phone Number',

        }

    def clean(self):
        cleaned_data = super().clean()
        max_guests = cleaned_data.get('max_guests')
        name = cleaned_data.get('name')
        location = cleaned_data.get('City')
        address = cleaned_data.get('address')
        price_per_night = cleaned_data.get('price_per_night')
        image_list = cleaned_data.get('image_list')
        description = cleaned_data.get('description')

        if image_list.len() == 0:
            raise ValidationError(
                "At least one image is required."
            )
        if max_guests <= 0:
            raise ValidationError(
                "Max guests must be a positive integer."
            )
