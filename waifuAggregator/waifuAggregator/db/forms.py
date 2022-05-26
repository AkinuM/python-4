from .models import pegs
from django.forms import ModelForm, TextInput, NumberInput

class pegsForm(ModelForm):
    class Meta:
        model = pegs
        fields = ['name', 'weight']

        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Peg name'
            }),
            'weight': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Peg weight'
            }),
        }