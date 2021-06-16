from django.db import models
from datetime import date

'''Справочники'''
class SprMarka(models.Model):
    naimmarka = models.CharField('Наименование марки тс', max_length=100)

    def __str__(self):
        return self.naimmarka, self.naimmodel

    def get_absolute_url(self):
        return f'/gruzi/{self.id}'

    class Meta:
        verbose_name = 'Марка тс'
        verbose_name_plural = 'Марки тс'

class SprModel(models.Model):
    naimmodel = models.CharField('Наименование модели тс', max_length=100)
    naimmarka = models.CharField('Наименование марки тс', max_length=100, default='')

    def __str__(self):
        return self.naimmodel

    def get_absolute_url(self):
        return f'/gruzi/{self.id}'

    class Meta:
        verbose_name = 'Модель тс'
        verbose_name_plural = 'Модели тс'

class Trsredstvo(models.Model):
    kod_ts = models.CharField('Гос номер', max_length=10, blank=True)
    gosnomer = models.CharField('Гос номер', max_length=10)

    naimmodel = models.CharField('Наименование модели тс', max_length=100, default='')
    naimmarka = models.CharField('Наименование марки тс', max_length=100, default='')

    naimvidts = models.CharField('Наименование вида ТС', max_length=100, default='')

    tipkuzova = models.CharField('Тип кузова', max_length=100, default='')
    gabdlina = models.CharField('Габариты длина', max_length=100, default='')
    gabshir = models.CharField('Габариты ширина', max_length=100, default='')
    gabvis = models.CharField('Габариты высота', max_length=100, default='')
    maxdopustmassa = models.CharField('Максимально допустимая масса', max_length=100, default='')
    sposobpogr = models.CharField('Способ погрузки', max_length=100, default='')

    def __str__(self):
        return self.gosnomer

    def get_absolute_url(self):
        return f'/gruzi/{self.id}'

    class Meta:
        verbose_name = 'Спр.транспортное средство'
        verbose_name_plural = 'Спр.транспортные средства'

class SprSotr(models.Model):
    kod_sotr = models.CharField('Код сотрудника', max_length=100)
    daterogd = models.DateField()
    fam = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    otch = models.CharField(max_length=50)

    datenaim = models.DateField()
    dateokonch = models.DateField(null=True, blank=True)

    dolgn = models.CharField(max_length=50)

    pasport = models.CharField(max_length=50)
    vodud = models.CharField(max_length=50)

    def __str__(self):
        return self.kod_sotr

    def get_absolute_url(self):
        return f'/gruzi/{self.id}'

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

class SprGorod(models.Model):
    naimgorod = models.CharField('Наименование города', max_length=100)

    def __str__(self):
        return self.naimgorod

    def get_absolute_url(self):
        return f'/gruzi/{self.id}'

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

class SprUlici(models.Model):
    naimulici = models.CharField('Наименование улицы', max_length=100)

    def __str__(self):
        return self.naimulici

    def get_absolute_url(self):
        return f'/gruzi/{self.id}'

    class Meta:
        verbose_name = 'Улица'
        verbose_name_plural = 'Улицы'

class SprDolgn(models.Model):
    naimdolgn = models.CharField('Наименование должности', max_length=100)

    def __str__(self):
        return self.naimdolgn

    def get_absolute_url(self):
        return f'/gruzi/{self.id}'

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'

class SprTipgruza(models.Model):
    naimtipgruza = models.CharField('Наименование типа груза', max_length=100)

    def __str__(self):
        return self.naimtipgruza

    def get_absolute_url(self):
        return f'/gruzi/{self.id}'

    class Meta:
        verbose_name = 'Тип груза'
        verbose_name_plural = 'Типы груза'

class SprGruza(models.Model):
    naimgruza = models.CharField('Наименование груза', max_length=100)
    edizm = models.CharField('Единица измерения', max_length=20)


    def __str__(self):
        return self.naimgruza

    def get_absolute_url(self):
        return f'/gruzi/{self.id}'

    class Meta:
        verbose_name = 'Груз'
        verbose_name_plural = 'Грузы'

class SprVidts(models.Model):
    naimvidts = models.CharField('Наименование вида ТС', max_length=100)

    def __str__(self):
        return self.naimvidts

    def get_absolute_url(self):
        return f'/gruzi/{self.id}'

    class Meta:
        verbose_name = 'Вид тс'
        verbose_name_plural = 'Виды тс'

class SprTovar(models.Model):
    naimtovar = models.CharField('Наименование товара', max_length=100)

    def __str__(self):
        return self.naimtovar

    def get_absolute_url(self):
        return f'/gruzi/{self.id}'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

class SprOrg(models.Model):
    naimorg = models.CharField('Наименование рганизации', max_length=100)

    def __str__(self):
        return self.naimorg

    def get_absolute_url(self):
        return f'/gruzi/{self.id}'

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'

class SprVidharts(models.Model):
    naimharts = models.CharField('Наименование характеристики ТС', max_length=100)

    def __str__(self):
        return self.naimharts

    def get_absolute_url(self):
        return f'/gruzi/{self.id}'

    class Meta:
        verbose_name = 'Наименование характеристики ТС'
        verbose_name_plural = 'Наименование характеристик ТС'

'''Основные'''

class Uchastnik(models.Model):
    viduch = models.CharField(max_length=100)
    org = models.CharField(max_length=100)
    inn = models.CharField(max_length=50)
    kpp = models.CharField(max_length=50)
    kontlico = models.CharField(max_length=100)
    tel = models.CharField(max_length=50)
    statusuch = models.CharField(max_length=100)

    def __str__(self):
        return self.viduch

    def get_absolute_url(self):
        return f'/gruzi/{self.id}'

    class Meta:
        verbose_name = 'Участник'
        verbose_name_plural = 'Участники'

class Zaiavka(models.Model):
    nomerzai = models.CharField(max_length=50)
    datezai = models.DateField()

    gruzopr = models.CharField(max_length=100)
    gruzpoluch = models.CharField(max_length=100)
    adr_gruzopr = models.CharField(max_length=100)
    adr_gruzpoluch = models.CharField(max_length=100)

    datepogr = models.DateField()
    daterazgr = models.DateField()
    statuszai = models.CharField(max_length=100)

    zakazch = models.CharField(max_length=100)

    naimgruza = models.CharField(max_length=100)
    edizm = models.CharField(max_length=100)
    kolvo = models.CharField(max_length=50)
    tipgruza = models.CharField(max_length=100)
    massa = models.CharField(max_length=50)
    gabdlina = models.CharField(max_length=50)
    gabshir = models.CharField(max_length=50)
    gabvisot = models.CharField(max_length=50)

    def __str__(self):
        return self.nomerzai

    def get_absolute_url(self):
        return f'/gruzi/{self.id}'

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

class Dogovor(models.Model):
    nomerdog = models.CharField(max_length=100)
    statusdog = models.CharField(max_length=100)
    stoimost = models.CharField(max_length=50)
    osobusl = models.CharField(max_length=500, null=True, blank=True)
    datesostdog = models.DateField()
    daterastdog = models.DateField(null=True, blank=True)
    datenachdog = models.DateField()
    dateokonchdog = models.DateField()
    datepodpdog = models.DateField()
    prichrast = models.CharField(max_length=100, null=True, blank=True)

    fiosotr = models.CharField(max_length=50)

    marka = models.CharField(max_length=50, blank=True)
    gosnomer = models.CharField(max_length=50, blank=True)

    nomerzai = models.CharField(max_length=50)
    datezai = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.nomerdog

    def get_absolute_url(self):
        return f'/gruzi/{self.id}'

    class Meta:
        verbose_name = 'Договор'
        verbose_name_plural = 'Договора'

'''Документы'''

class Putlist(models.Model):
    nomerdog = models.ForeignKey(Dogovor, on_delete=models.PROTECT)

    nomerputlist = models.CharField(max_length=50)
    datesostputlist = models.DateField()
    statusputlist = models.CharField(max_length=100)
    dateviezd = models.DateField()
    nachpokazodo = models.CharField(max_length=50)
    datevozvr = models.DateField()
    konechpokazodo = models.CharField(max_length=50)
    ostgoruchviezd = models.CharField(max_length=50)
    ostgoruchvozvr = models.CharField(max_length=50)
    srokputlist = models.CharField(max_length=100)


    def __str__(self):
        return self.nomerdog, self.nomerputlist

    def get_absolute_url(self):
        return f'/gruzi/{self.id}'

    class Meta:
        verbose_name = 'Путевой лист'
        verbose_name_plural = 'Путевые листы'

class Schetfact(models.Model):
    nomerdog = models.ForeignKey(Dogovor, on_delete=models.PROTECT, default='')

    nomerschetfact = models.CharField(max_length=50)
    datesostschetfact = models.DateField()
    statusschetfact = models.CharField(max_length=100)
    nalstav =  models.CharField(max_length=50)
    stoimostt = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.nomerschetfact

    def get_absolute_url(self):
        return f'/gruzi/{self.id}'

    class Meta:
        verbose_name = 'Счет фактура'
        verbose_name_plural = 'Счет фактуры'

class Actovipoln(models.Model):
    nomerdog = models.ForeignKey(Dogovor, on_delete=models.PROTECT, default='')

    nomeract = models.CharField(max_length=100)
    dateact = models.DateField()
    statusact = models.CharField(max_length=100)
    dates = models.DateField()
    datepo = models.DateField()
    pretenz = models.CharField(max_length=100, blank=True)
    datepodpis = models.DateField(null=True, blank=True)

    zakazch = models.CharField(max_length=100, blank=True)
    fios = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.nomeract

    def get_absolute_url(self):
        return f'/gruzi/{self.id}'

    class Meta:
        verbose_name = 'Акт о выполненной работе'
        verbose_name_plural = 'Акты о выполненной работе'

class Schetopl(models.Model):
    nomerschet = models.CharField(max_length=50)

    nomerdog = models.ForeignKey(Dogovor, on_delete=models.CASCADE)

    dateschet = models.DateField()
    statusschet = models.CharField(max_length=100)
    nomerschetpoluch = models.CharField(max_length=50)
    summa = models.CharField(max_length=50)
    poluchatel = models.CharField(max_length=100)

    zakazch = models.CharField(max_length=100, blank=True)
    bank = models.CharField(max_length=100, blank=True)
    schetbanka = models.CharField(max_length=100, blank=True)
    bik = models.CharField(max_length=100, blank=True)

    sostavil = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.nomerschet

    def get_absolute_url(self):
        return f'/gruzi/{self.id}'

    class Meta:
        verbose_name = 'Счет на оплату'
        verbose_name_plural = 'Счет на оплату'

class Ttn(models.Model):

    nomerttn = models.CharField(max_length=50)
    datettn = models.DateField()
    statusttn = models.CharField(max_length=100)
    kolvoplan = models.CharField(max_length=50)
    kolvofact = models.CharField(max_length=50)
    edizmttn = models.CharField(max_length=100)
    srokdost = models.DateField(max_length=100)
    itogstoim = models.CharField(max_length=50)

    def __str__(self):
        return self.nomerttn

    def get_absolute_url(self):
        return f'/gruzi/{self.id}'

    class Meta:
        verbose_name = 'ттн'
        verbose_name_plural = 'ттн'




