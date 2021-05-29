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



    def __str__(self):
        return self.naimmodel

    def get_absolute_url(self):
        return f'/gruzi/{self.id}'

    class Meta:
        verbose_name = 'Модель тс'
        verbose_name_plural = 'Модели тс'

class Trsredstvo(models.Model):
    gosnomer = models.CharField('Гос номер', max_length=10)

    def __str__(self):
        return self.gosnomer

    def get_absolute_url(self):
        return f'/gruzi/{self.id}'

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

class SprSotr(models.Model):
    kod_sotr = models.PositiveIntegerField()
    daterogd = models.DateField()
    fam = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    otch = models.CharField(max_length=50)

    datenaim = models.DateField()
    dateokonch = models.DateField()

    dolgn = models.CharField(max_length=50)

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
    inn = models.PositiveIntegerField()
    kpp = models.PositiveIntegerField()
    kontlico = models.CharField(max_length=100)
    tel = models.PositiveIntegerField()
    statusuch = models.CharField(max_length=100)

    def __str__(self):
        return self.viduch

    def get_absolute_url(self):
        return f'/gruzi/{self.id}'

    class Meta:
        verbose_name = 'Участник'
        verbose_name_plural = 'Участники'

class Zaiavka(models.Model):
    nomerzai = models.CharField(max_length=100)
    datezai = models.DateField()

    gruzopr = models.CharField(max_length=100)
    gruzpoluch = models.CharField(max_length=100)
    adr_gruzopr = models.CharField(max_length=100)
    adr_gruzpoluch = models.CharField(max_length=100)

    datepogr = models.DateField()
    daterazgr = models.CharField(max_length=100)
    statuszai = models.CharField(max_length=100)

    zakazch = models.CharField(max_length=100)

    naimgruza = models.CharField(max_length=100)
    edizm = models.CharField(max_length=100)
    kolvo = models.PositiveIntegerField()
    tipgruza = models.CharField(max_length=100)
    massa = models.DecimalField(max_digits=2, decimal_places=2)
    gabdlina = models.DecimalField(max_digits=2, decimal_places=2)
    gabshir = models.DecimalField(max_digits=2, decimal_places=2)
    gabvisot = models.DecimalField(max_digits=2, decimal_places=2)

    def __str__(self):
        return self.nomerzai

    def get_absolute_url(self):
        return f'/gruzi/{self.id}'

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

class Dogovor(models.Model):
    nomerdog = models.PositiveIntegerField()
    statusdog = models.CharField(max_length=100)
    stoimost = models.PositiveIntegerField()
    osobusl = models.PositiveIntegerField()
    datesostdog = models.DateField(max_length=100)
    daterastdog = models.DateField()
    datenachdog = models.DateField()
    dateokonchdog = models.DateField(default=False)
    datepodpdog = models.DateField(default=False)
    prichrast = models.CharField(max_length=100)

    kod_sotr = models.PositiveIntegerField()
    kod_ts = models.PositiveIntegerField()

    def __str__(self):
        return self.viduch

    def get_absolute_url(self):
        return f'/gruzi/{self.id}'

    class Meta:
        verbose_name = 'Участник'
        verbose_name_plural = 'Участники'

'''Документы'''

class Putlist(models.Model):
    nomerdog = models.PositiveIntegerField()

    nomerputlist = models.PositiveIntegerField()
    datesostputlist = models.DateField()
    statusputlist = models.CharField(max_length=100)
    dateviezd = models.DateField()
    nachpokazodo = models.PositiveIntegerField()
    datevozvr = models.DateField()
    konechpokazodo = models.PositiveIntegerField()
    ostgoruchviezd = models.PositiveIntegerField()
    ostgoruchvozvr = models.PositiveIntegerField()
    srokputlist = models.CharField(max_length=100)

    def __str__(self):
        return self.nomerdog, self.nomerputlist

    def get_absolute_url(self):
        return f'/gruzi/{self.id}'

    class Meta:
        verbose_name = 'ттн'
        verbose_name_plural = 'ттн'

class Schetfact(models.Model):
    nomerschetfact = models.PositiveIntegerField()
    datesostschetfact = models.DateField()
    statusschetfact = models.CharField(max_length=100)
    nalstav =  models.DecimalField(max_digits=2, decimal_places=2)

    def __str__(self):
        return self.nomerschetfact

    def get_absolute_url(self):
        return f'/gruzi/{self.id}'

    class Meta:
        verbose_name = 'Счет фактура'
        verbose_name_plural = 'Счет фактура'

class Actovipoln(models.Model):
    nomeract = models.PositiveIntegerField()
    dateact = models.DateField()
    statusact = models.CharField(max_length=100)
    dates = models.DateField()
    datepo = models.DateField()

    def __str__(self):
        return self.nomeract

    def get_absolute_url(self):
        return f'/gruzi/{self.id}'

    class Meta:
        verbose_name = 'Акт о выполненной работе'
        verbose_name_plural = 'Акт о выполненной работе'

class Schetopl(models.Model):
    nomerschet = models.PositiveIntegerField()
    dateschet = models.DateField()
    statusschet = models.CharField(max_length=100)
    nomerschetpoluch = models.PositiveIntegerField()
    summa = models.PositiveIntegerField()
    poluchatel = models.CharField(max_length=100)

    def __str__(self):
        return self.nomerschet

    def get_absolute_url(self):
        return f'/gruzi/{self.id}'

    class Meta:
        verbose_name = 'Счет на оплату'
        verbose_name_plural = 'Счет на оплату'

class Ttn(models.Model):
    nomerttn = models.PositiveIntegerField()
    datettn = models.DateField()
    statusttn = models.CharField(max_length=100)
    kolvoplan = models.PositiveIntegerField()
    kolvofact = models.PositiveIntegerField()
    edizmttn = models.CharField(max_length=100)
    srokdost = models.DateField(max_length=100)
    itogstoim = models.PositiveIntegerField()

    def __str__(self):
        return self.nomerttn

    def get_absolute_url(self):
        return f'/gruzi/{self.id}'

    class Meta:
        verbose_name = 'ттн'
        verbose_name_plural = 'ттн'




