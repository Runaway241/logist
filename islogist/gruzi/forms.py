from .models import *
from django.forms import ModelForm, TextInput, DateField, CheckboxInput, DateInput, Select, NumberInput

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

class addzaiavkarForm(ModelForm):
    class Meta:
        fields = ['nomerzai', 'datezai', 'gruzopr', 'gruzpoluch', 'adr_gruzopr', 'adr_gruzpoluch', 'datepogr',
                  'daterazgr', 'statuszai', 'zakazch', 'naimgruza', 'edizm', 'kolvo', 'tipgruza', 'massa', 'gabdlina', 'gabshir', 'gabvisot']
        model = Zaiavka
        widgets = {
            'nomerzai': TextInput(attrs={
            'class': 'form-control'
            }),
            'datezai': DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'gruzopr': TextInput(attrs={
                'class': 'form-control'
            }),
            'gruzpoluch': TextInput(attrs={
                'class': 'form-control'
            }),
            'adr_gruzopr': TextInput(attrs={
                'class': 'form-control'
            }),
            'adr_gruzpoluch': TextInput(attrs={
                'class': 'form-control'
            }),
            'datepogr': DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'daterazgr': DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'statuszai': TextInput(attrs={
                'class': 'form-control'
            }),
            'zakazch': TextInput(attrs={
                'class': 'form-control'
            }),
            'naimgruza': TextInput(attrs={
                'class': 'form-control'
            }),
            'edizm': TextInput(attrs={
                'class': 'form-control'
            }),
            'kolvo': TextInput(attrs={
                'class': 'form-control'
            }),
            'tipgruza': TextInput(attrs={
                'class': 'form-control'
            }),
            'massa': TextInput(attrs={
                'class': 'form-control'
            }),
            'gabdlina': TextInput(attrs={
                'class': 'form-control'
            }),
            'gabshir': TextInput(attrs={
                'class': 'form-control'
            }),
            'gabvisot': TextInput(attrs={
                'class': 'form-control'
            }),
        }

class adddogovorForm(ModelForm):
    class Meta:
        fields = ['nomerdog', 'statusdog', 'stoimost', 'osobusl', 'datesostdog', 'daterastdog', 'datenachdog',
                  'dateokonchdog', 'datepodpdog', 'prichrast', 'kod_sotr', 'kod_ts']
        model = Dogovor
        widgets = {
            'nomerdog': TextInput(attrs={
            'class': 'form-control'
            }),
            'statusdog': DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'stoimost': TextInput(attrs={
                'class': 'form-control'
            }),
            'osobusl': TextInput(attrs={
                'class': 'form-control'
            }),
            'datesostdog': TextInput(attrs={
                'class': 'form-control'
            }),
            'daterastdog': TextInput(attrs={
                'class': 'form-control'
            }),
            'datenachdog': DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'dateokonchdog': DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'datepodpdog': TextInput(attrs={
                'class': 'form-control'
            }),
            'prichrast': TextInput(attrs={
                'class': 'form-control'
            }),
            'kod_sotr': TextInput(attrs={
                'class': 'form-control'
            }),
            'kod_ts': TextInput(attrs={
                'class': 'form-control'
            }),

        }

class addsprsotrForm(ModelForm):
    class Meta:
        fields = ['kod_sotr', 'daterogd', 'fam', 'name', 'otch', 'datenaim', 'dateokonch', 'dolgn']
        model = SprSotr
        widgets = {
            'kod_sotr': TextInput(attrs={
            'class': 'form-control'
            }),
            'daterogd': DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'fam': TextInput(attrs={
                'class': 'form-control'
            }),
            'name': TextInput(attrs={
                'class': 'form-control'
            }),
            'otch': TextInput(attrs={
                'class': 'form-control'
            }),
            'datenaim': DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'dateokonch': DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'dolgn': TextInput(attrs={
                'class': 'form-control'
            }),
        }
