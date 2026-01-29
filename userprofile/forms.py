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
        fields = ['first_name', 'last_name', 'email', 'phone_number',]
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
            'phone_number': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Enter your phone number'}),
        }

        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',

        }

    def clean(self):
        """Validate form data for profile fields only"""
        cleaned_data = super().clean()
        
        # Add any profile-specific validation here if needed
        # (guests validation removed - that belongs in booking forms)
        
        return cleaned_data

    def save(self, commit=True):
        """Save profile and update user name"""
        user = self.instance.user
        user.first_name = self.cleaned_data.get('first_name', '')
        user.last_name = self.cleaned_data.get('last_name', '')

        user.save()

        return super().save(commit=commit)

