from django import forms
from .models import Pendiente

class PendienteForm(forms.ModelForm):
    class Meta:
        model = Pendiente
        fields = ['title', 'description', 'resuelto']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Título del pendiente',
                'required': True
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Descripción del pendiente (opcional)',
                'rows': 4
            }),
            'resuelto': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            })
        }
        labels = {
            'title': 'Título',
            'description': 'Descripción',
            'resuelto': 'Marcar como resuelto'
        }