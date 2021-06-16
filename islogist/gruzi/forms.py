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
                  'dateokonchdog', 'datepodpdog', 'prichrast', 'fiosotr', 'marka', 'gosnomer', 'nomerzai', 'datezai']
        model = Dogovor
        widgets = {
            'nomerdog': TextInput(attrs={
            'class': 'form-control'
            }),
            'statusdog': TextInput(attrs={
                'class': 'form-control'

            }),
            'stoimost': TextInput(attrs={
                'class': 'form-control'
            }),
            'osobusl': TextInput(attrs={
                'class': 'form-control'
            }),
            'datesostdog': DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'daterastdog': DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'datenachdog': DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'dateokonchdog': DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'datepodpdog': DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
            }),
            'prichrast': TextInput(attrs={
                'class': 'form-control'
            }),
            'fiosotr': TextInput(attrs={
                'class': 'form-control'
            }),
            'marka': TextInput(attrs={
                'class': 'form-control'
            }),
            'gosnomer': TextInput(attrs={
            'nomerzai': TextInput(attrs={
                'class': 'form-control'
            }),
            'datezai': DateInput(attrs={
                'class': 'form-control',
                'type':'date',
            }),
            }),
        }

class addsprsotrForm(ModelForm):
    class Meta:
        fields = ['kod_sotr', 'daterogd', 'fam', 'name', 'otch', 'datenaim', 'dateokonch', 'dolgn','pasport','vodud']
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
            'pasport': TextInput(attrs={
                'class': 'form-control'
            }),
            'vodud': TextInput(attrs={
                'class': 'form-control'
            }),
        }

class addactovipolnForm(ModelForm):
    class Meta:
        fields = ['nomeract', 'dateact', 'statusact', 'dates', 'datepo', 'pretenz', 'datepodpis', 'zakazch','fios']
        model = Actovipoln
        widgets = {
            'nomeract': TextInput(attrs={
            'class': 'form-control'
            }),
            'dateact': DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'statusact': TextInput(attrs={
                'class': 'form-control'
            }),
            'dates': DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'datepo': DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'pretenz': TextInput(attrs={
                'class': 'form-control'

            }),
            'datepodpis': DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'zakazch': TextInput(attrs={
                'class': 'form-control'
            }),
            'fios': TextInput(attrs={
                'class': 'form-control'
            }),
        }

class addschetoplForm(ModelForm):
    class Meta:
        fields = ['nomerschet', 'nomerdog', 'dateschet', 'statusschet', 'nomerschetpoluch', 'summa', 'poluchatel', 'zakazch','bank', 'schetbanka','bik', 'sostavil']
        model = Schetopl
        widgets = {
            'nomerschet': TextInput(attrs={
                'class': 'form-control'
            }),
            'nomerdog': TextInput(attrs={
                'class': 'form-control'
            }),
            'dateschet': DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'statusschet': TextInput(attrs={
                'class': 'form-control'
            }),
            'nomerschetpoluch': TextInput(attrs={
                'class': 'form-control'
            }),
            'summa': TextInput(attrs={
                'class': 'form-control'

            }),
            'poluchatel': TextInput(attrs={
                'class': 'form-control'

            }),
            'zakazch': TextInput(attrs={
                'class': 'form-control'
            }),
            'bank': TextInput(attrs={
                'class': 'form-control'
            }),
            'schetbanka': TextInput(attrs={
                'class': 'form-control'
            }),
            'bik': TextInput(attrs={
                'class': 'form-control'
            }),
            'sostavil': TextInput(attrs={
                'class': 'form-control'
            }),
        }

class addschetfactForm(ModelForm):
    class Meta:
        fields = ['nomerdog', 'nomerschetfact', 'datesostschetfact', 'statusschetfact', 'nalstav', 'stoimostt']
        model = Schetfact
        widgets = {
            'nomerdog': TextInput(attrs={
                'class': 'form-control'
            }),
            'nomerschetfact': TextInput(attrs={
                'class': 'form-control'
            }),
            'datesostschetfact': DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'statusschetfact': TextInput(attrs={
                'class': 'form-control'
            }),
            'nalstav': TextInput(attrs={
                'class': 'form-control'
            }),
            'stoimostt': TextInput(attrs={
                'class': 'form-control'

            }),
        }

class addputlistForm(ModelForm):
    class Meta:
        fields = ['nomerdog', 'nomerputlist', 'datesostputlist', 'statusputlist', 'dateviezd',
                  'nachpokazodo', 'datevozvr', 'konechpokazodo', 'ostgoruchviezd', 'ostgoruchvozvr', 'srokputlist']
        model = Putlist
        widgets = {
            'nomerdog': Select(attrs={
                'class': 'form-control'
            }),
            'nomerputlist': TextInput(attrs={
                'class': 'form-control'
            }),
            'datesostputlist': DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'statusputlist': TextInput(attrs={
                'class': 'form-control'
            }),
            'dateviezd': DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'nachpokazodo': TextInput(attrs={
                'class': 'form-control'

            }),
            'datevozvr': DateInput(attrs={
                'class': 'form-control',
                'type': 'date'

            }),
            'konechpokazodo': TextInput(attrs={
                'class': 'form-control'

            }),
            'ostgoruchviezd': TextInput(attrs={
                'class': 'form-control'

            }),
            'ostgoruchvozvr': TextInput(attrs={
                'class': 'form-control'

            }),
            'srokputlist': TextInput(attrs={
                'class': 'form-control'

            }),
        }