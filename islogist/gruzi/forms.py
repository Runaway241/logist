from .models import *
from django.forms import ModelForm,TextInput, CheckboxInput, DateInput, Select, NumberInput

class adduchastnikForm(ModelForm):
    class Meta:
        fields = ['viduch', 'org', 'inn', 'kpp', 'kontlico', 'tel', 'statusuch']
        model = Uchastnik
        widgets = {
            'viduch': TextInput(attrs={
            'class': 'form-control'
            }),
            'org': TextInput(attrs={
                'class': 'form-control'
            }),
            'inn': TextInput(attrs={
                'class': 'form-control'
            }),
            'kpp': TextInput(attrs={
                'class': 'form-control'
            }),
            'kontlico': TextInput(attrs={
                'class': 'form-control'
            }),
            'tel': TextInput(attrs={
                'class': 'form-control'
            }),
            'statusuch': TextInput(attrs={
                'class': 'form-control'
            }),
        }
