# Generated by Django 3.2.3 on 2021-05-31 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gruzi', '0008_auto_20210531_2135'),
    ]

    operations = [
        migrations.AddField(
            model_name='schetopl',
            name='bik',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
