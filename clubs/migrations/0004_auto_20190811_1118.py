# Generated by Django 2.2.1 on 2019-08-11 11:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0003_auto_20190811_1116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deals',
            name='startTime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
