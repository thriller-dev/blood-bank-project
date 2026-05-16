from django import forms
from .models import Donor

class DonorRegistrationForm(forms.ModelForm):
    class Meta:
        model = Donor
        fields = ['full_name', 'age', 'gender', 'blood_group', 'phone_number', 'email', 'city', 'last_donation_date', 'is_available']
        widgets = {
            'last_donation_date': forms.DateInput(attrs={'type': 'date'}),
        }
