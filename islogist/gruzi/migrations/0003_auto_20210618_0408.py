# Generated by Django 3.2.3 on 2021-06-18 01:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gruzi', '0002_auto_20210618_0020'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dogovor',
            name='gosnomer',
        ),
        migrations.RemoveField(
            model_name='dogovor',
            name='marka',
        ),
        migrations.AddField(
            model_name='dogovor',
            name='kod_ts',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='gruzi.trsredstvo'),
        ),
        migrations.AlterField(
            model_name='dogovor',
            name='dateokonchdog',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='dogovor',
            name='fiosotr',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gruzi.sprsotr'),
        ),
        migrations.AlterField(
            model_name='dogovor',
            name='nomerzai',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gruzi.zaiavka'),
        ),
        migrations.AlterField(
            model_name='uchastnik',
            name='org',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gruzi.sprorg'),
        ),
        migrations.AlterField(
            model_name='zaiavka',
            name='gruzopr',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='oprgruza', to='gruzi.uchastnik'),
        ),
        migrations.AlterField(
            model_name='zaiavka',
            name='gruzpoluch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='poluchgruza', to='gruzi.uchastnik'),
        ),
        migrations.AlterField(
            model_name='zaiavka',
            name='naimgruza',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gruzi.sprgruza'),
        ),
        migrations.AlterField(
            model_name='zaiavka',
            name='nomerzai',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='zaiavka',
            name='tipgruza',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gruzi.sprtipgruza'),
        ),
        migrations.AlterField(
            model_name='zaiavka',
            name='zakazch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gruzi.sprorg'),
        ),
    ]
