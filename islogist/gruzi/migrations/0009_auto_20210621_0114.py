# Generated by Django 3.2.3 on 2021-06-20 22:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gruzi', '0008_otchdoglog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dogovor',
            name='dateokonchdog',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dogovor',
            name='statusdog',
            field=models.CharField(choices=[('tekuch', 'Текущий'), ('vipoln', 'Выполненный')], default='tekuch', max_length=100),
        ),
        migrations.AlterField(
            model_name='sprsotr',
            name='vodud',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='trsredstvo',
            name='naimmarka',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gruzi.sprmarka'),
        ),
        migrations.AlterField(
            model_name='trsredstvo',
            name='sposobpogr',
            field=models.CharField(choices=[('Verhn', 'Верхняя'), ('Bokov', 'Боковая'), ('Zadn', 'Задняя')], default='', max_length=100, verbose_name='Способ погрузки'),
        ),
        migrations.AlterField(
            model_name='zaiavka',
            name='statuszai',
            field=models.CharField(choices=[('odobr', 'Одобрено'), ('otkl', 'Отклонено')], max_length=100),
        ),
    ]
