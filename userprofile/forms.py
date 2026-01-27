from django import forms
import re
from .models import UserProfile
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm


class ProfileSetupForm(forms.ModelForm):
    """Form for setting up user profile"""

    class Meta:
        model = UserProfile
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
        guests = cleaned_data.get('guests')
        # Assuming there's a field for property limit
        property_limit = cleaned_data.get('')

        # Validate age
        if guests and (guests < 1 or guests > 2):
            self.add_error(
                'guests', 'number of maximum guests per room should 2.')
        elif guests > 2 and guests <= 5:  # Special case for more than 2 guests according to property limit
            self.add_error(
                'guests', 'For more than 2 guests, please contact support.')

    def save(self, commit=True):
        """Save profile and update user name"""
        user = self.instance.user
        user.first_name = self.cleaned_data.get('first_name', '')
        user.last_name = self.cleaned_data.get('last_name', '')

        user.save()

        return super().save(commit=commit)
