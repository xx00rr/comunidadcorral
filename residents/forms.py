from django import forms
from .models import Resident
from units.models import Unit

_fc = {'class': 'form-control'}
_fs = {'class': 'form-select'}


class ResidentForm(forms.ModelForm):
    class Meta:
        model = Resident
        fields = ['unit', 'first_name', 'last_name', 'email', 'phone',
                  'identification', 'role', 'status', 'move_in_date', 'move_out_date', 'notes']
        widgets = {
            'unit': forms.Select(attrs=_fs),
            'first_name': forms.TextInput(attrs=_fc),
            'last_name': forms.TextInput(attrs=_fc),
            'email': forms.EmailInput(attrs=_fc),
            'phone': forms.TextInput(attrs=_fc),
            'identification': forms.TextInput(attrs=_fc),
            'role': forms.Select(attrs=_fs),
            'status': forms.Select(attrs=_fs),
            'move_in_date': forms.DateInput(attrs={**_fc, 'type': 'date'}),
            'move_out_date': forms.DateInput(attrs={**_fc, 'type': 'date'}),
            'notes': forms.Textarea(attrs={**_fc, 'rows': 3}),
        }

    def __init__(self, *args, organization=None, initial_unit=None, **kwargs):
        super().__init__(*args, **kwargs)
        if organization:
            self.fields['unit'].queryset = Unit.objects.filter(organization=organization)
        if initial_unit:
            self.fields['unit'].initial = initial_unit
