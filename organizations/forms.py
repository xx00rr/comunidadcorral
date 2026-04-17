from django import forms
from .models import Organization

_fc = {'class': 'form-control'}


class OrganizationForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = ['name', 'address', 'contact_email', 'contact_phone']
        widgets = {
            'name': forms.TextInput(attrs=_fc),
            'address': forms.TextInput(attrs=_fc),
            'contact_email': forms.EmailInput(attrs=_fc),
            'contact_phone': forms.TextInput(attrs=_fc),
        }
