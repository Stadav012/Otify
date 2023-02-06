from django import forms
from .models import Complaint

class ComplainForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['category', 'date', 'description', 'region']