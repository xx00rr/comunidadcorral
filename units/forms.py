from django import forms
from .models import Unit

_fc = {'class': 'form-control'}
_fs = {'class': 'form-select'}


class UnitForm(forms.ModelForm):
    class Meta:
        model = Unit
        fields = ['identifier', 'unit_type', 'status', 'floor', 'area_m2', 'notes']
        widgets = {
            'identifier': forms.TextInput(attrs=_fc),
            'unit_type': forms.Select(attrs=_fs),
            'status': forms.Select(attrs=_fs),
            'floor': forms.TextInput(attrs=_fc),
            'area_m2': forms.NumberInput(attrs=_fc),
            'notes': forms.Textarea(attrs={**_fc, 'rows': 3}),
        }
