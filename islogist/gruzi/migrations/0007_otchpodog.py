# Generated by Django 3.2.3 on 2021-06-18 04:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gruzi', '0006_ttn_nomerdog'),
    ]

    operations = [
        migrations.CreateModel(
            name='Otchpodog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dates', models.DateField()),
                ('datepo', models.DateField()),
                ('datesostavl', models.DateField()),
                ('datenachala', models.DateField()),
                ('dateokonch', models.DateField()),
                ('stoimostt', models.CharField(max_length=100)),
                ('nomerdog', models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='gruzi.dogovor')),
                ('sformir', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gruzi.sprsotr')),
            ],
            options={
                'verbose_name': 'Отчет по заключенным договорам',
                'verbose_name_plural': 'Отчет по заключенным договорам',
            },
        ),
    ]
