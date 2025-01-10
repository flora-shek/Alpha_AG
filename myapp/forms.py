from django import forms
from .models import Prayer_request

class PrayerForm(forms.ModelForm):
    class Meta:
        model = Prayer_request
        fields = ['email', 'request']
        
