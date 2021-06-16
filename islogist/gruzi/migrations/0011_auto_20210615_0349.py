# Generated by Django 3.2.3 on 2021-06-15 00:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gruzi', '0010_alter_sprsotr_dateokonch'),
    ]

    operations = [
        migrations.AddField(
            model_name='schetfact',
            name='nomerdog',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='gruzi.dogovor'),
        ),
        migrations.AddField(
            model_name='schetfact',
            name='stoimostt',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='actovipoln',
            name='nomeract',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='putlist',
            name='nomerdog',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gruzi.dogovor'),
        ),
        migrations.AlterField(
            model_name='schetopl',
            name='nomerdog',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gruzi.dogovor'),
        ),
    ]