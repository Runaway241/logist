from .models import *
from django.forms import ModelForm, TextInput, DateField, CheckboxInput, DateInput, Select, NumberInput
class addtrsredstvoForm(ModelForm):
    class Meta:
        fields = ['kod_ts', 'gosnomer', 'naimmodel', 'naimmarka', 'naimvidts', 'tipkuzova', 'gabdlina',
                  'gabshir', 'gabvis', 'maxdopustmassa', 'sposobpogr']
        model = Trsredstvo
        widgets = {
            'kod_ts': TextInput(attrs={
            'class': 'form-control'
            }),
            'gosnomer': TextInput(attrs={
                'class': 'form-control'
            }),
            'naimmodel': Select(attrs={
                'class': 'form-control'
            }),
            'naimmarka': Select(attrs={
                'class': 'form-control'
            }),
            'naimvidts': Select(attrs={
                'class': 'form-control'
            }),
            'tipkuzova': Select(attrs={
                'class': 'form-control'
            }),
            'gabdlina': TextInput(attrs={
                'class': 'form-control'
            }),
            'gabshir': TextInput(attrs={
                'class': 'form-control'
            }),

            'gabvis': TextInput(attrs={
                'class': 'form-control'
            }),

            'maxdopustmassa': TextInput(attrs={
                'class': 'form-control'
            }),

            'sposobpogr': Select(attrs={
                'class': 'form-control'
            }),

        }

class addmodelForm(ModelForm):
    class Meta:
        fields = ['naimmodel']
        model = SprModel
        widgets = {
            'naimmodel': TextInput(attrs={
            'class': 'form-control'
            }),
        }

class addorgForm(ModelForm):
    class Meta:
        fields = ['naimorg']
        model = SprOrg
        widgets = {
            'naimorg': TextInput(attrs={
            'class': 'form-control'
            }),
        }

class addmarkaForm(ModelForm):
    class Meta:
        fields = ['naimmarka', 'naimmodel']
        model = SprMarka
        widgets = {
            'naimmarka': TextInput(attrs={
                'class': 'form-control'
            }),
            'naimmodel': Select(attrs={
            'class': 'form-control'
            }),
        }

class adddolgnForm(ModelForm):
    class Meta:
        fields = ['naimdolgn']
        model = SprDolgn
        widgets = {
            'naimdolgn': TextInput(attrs={
                'class': 'form-control'
            }),
        }

class addtipgruzaForm(ModelForm):
    class Meta:
        fields = ['naimtipgruza']
        model = SprTipgruza
        widgets = {
            'naimtipgruza': TextInput(attrs={
                'class': 'form-control'
            }),
        }

class adduchastnikForm(ModelForm):
    class Meta:
        fields = ['viduch', 'org', 'inn', 'kpp', 'kontlico', 'tel']
        model = Uchastnik
        widgets = {
            'viduch': TextInput(attrs={
            'class': 'form-control'
            }),
            'org': Select(attrs={
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
            'gruzopr': Select(attrs={
                'class': 'form-control'
            }),
            'gruzpoluch': Select(attrs={
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
            'statuszai': Select(attrs={
                'class': 'form-control'
            }),
            'zakazch': Select(attrs={
                'class': 'form-control'
            }),
            'naimgruza': Select(attrs={
                'class': 'form-control'
            }),
            'edizm': TextInput(attrs={
                'class': 'form-control'
            }),
            'kolvo': TextInput(attrs={
                'class': 'form-control'
            }),
            'tipgruza': Select(attrs={
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
        fields = ['nomerzai', 'nomerdog', 'statusdog', 'stoimost', 'osobusl', 'datesostdog', 'daterastdog', 'datenachdog',
                  'dateokonchdog', 'datepodpdog', 'prichrast', 'fiosotr','kod_ts']
        model = Dogovor
        widgets = {
            'nomerzai': Select(attrs={
                'class': 'form-control'
            }),
            'nomerdog': TextInput(attrs={
            'class': 'form-control'
            }),
            'statusdog': Select(attrs={
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
            'fiosotr': Select(attrs={
                'class': 'form-control'
            }),
            'kod_ts': Select(attrs={
                'class': 'form-control'
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
        fields = ['nomerdog', 'nomeract', 'dateact', 'statusact', 'dates', 'datepo', 'pretenz', 'datepodpis', 'zakazch','fios']
        model = Actovipoln
        widgets = {
            'nomerdog': Select(attrs={
                'class': 'form-control'
            }),

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
            'zakazch': Select(attrs={
                'class': 'form-control'
            }),
            'fios': Select(attrs={
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
            'nomerdog': Select(attrs={
                'class': 'form-control'
            }),
            'dateschet': DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'statusschet': Select(attrs={
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
            'datepodpisschetopl': TextInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'sostavil': TextInput(attrs={
                'class': 'form-control'
            }),
        }

class addschetfactForm(ModelForm):
    class Meta:
        fields = ['nomerdog', 'nomerschetfact', 'datesostschetfact', 'statusschetfact', 'nalstav', 'stoimostt',
                  'datepodpschetfact', 'sostschetfact']
        model = Schetfact
        widgets = {
            'nomerdog': Select(attrs={
                'class': 'form-control'
            }),
            'nomerschetfact': TextInput(attrs={
                'class': 'form-control'
            }),
            'datesostschetfact': DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'statusschetfact': Select(attrs={
                'class': 'form-control'
            }),
            'nalstav': TextInput(attrs={
                'class': 'form-control'
            }),
            'stoimostt': TextInput(attrs={
                'class': 'form-control'

            }),
            'datepodpschetfact': DateInput(attrs={
                'class': 'form-control',
                'type': 'date'

            }),
            'sostschetfact': Select(attrs={
                'class': 'form-control'

            }),
        }

class addputlistForm(ModelForm):
    class Meta:
        fields = ['nomerdog', 'nomerputlist', 'datesostputlist', 'statusputlist', 'dateviezd',
                  'nachpokazodo', 'datevozvr', 'konechpokazodo', 'ostgoruchviezd', 'ostgoruchvozvr', 'srokputlist',
                  'datepodpputlist', 'osobotm']
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
            'datepodpputlist': DateInput(attrs={
                'class': 'form-control',
                'type': 'date'

            }),
            'osobotm': TextInput(attrs={
                'class': 'form-control'

            }),
        }

class addttnForm(ModelForm):
    class Meta:
        fields = ['nomerdog', 'nomerttn', 'datettn', 'statusttn', 'naimgruz', 'kolvoplan',
                  'kolvofact', 'edizmttn', 'srokdost', 'itogstoim']
        model = Ttn
        widgets = {
            'nomerdog': Select(attrs={
                'class': 'form-control'
            }),
            'nomerttn': TextInput(attrs={
                'class': 'form-control'
            }),
            'datettn': DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'statusttn': TextInput(attrs={
                'class': 'form-control'
            }),
            'naimgruz': Select(attrs={
                'class': 'form-control'
            }),
            'kolvoplan': DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'kolvofact': TextInput(attrs={
                'class': 'form-control'

            }),
            'edizmttn': DateInput(attrs={
                'class': 'form-control',
                'type': 'date'

            }),
            'srokdost': DateInput(attrs={
                'class': 'form-control',
                'type': 'date'

            }),
            'itogstoim': TextInput(attrs={
                'class': 'form-control'

            }),

        }

class addotchpodogForm(ModelForm):
    class Meta:
        fields = ['nomerdog', 'dates', 'datepo', 'datepo', 'stoimostt',
                  'sformir']
        model = Otchpodog
        widgets = {

            'dates': DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'datepo': DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
        }

class addotchdoglogForm(ModelForm):
    class Meta:
        fields = ['nomerdog', 'datess', 'dateppo', 'datesostavll',
                  'stoimosttt', 'sformirr']
        model = Otchdoglog
        widgets = {
            'datess': DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'dateppo': DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
        }