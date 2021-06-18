# Generated by Django 3.2.3 on 2021-06-17 21:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gruzi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sprmodel',
            name='naimmarka',
        ),
        migrations.AddField(
            model_name='sprmarka',
            name='naimmodel',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='gruzi.sprmodel'),
        ),
        migrations.AlterField(
            model_name='trsredstvo',
            name='naimmodel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gruzi.sprmodel'),
        ),
        migrations.AlterField(
            model_name='trsredstvo',
            name='naimvidts',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gruzi.sprvidts'),
        ),
    ]