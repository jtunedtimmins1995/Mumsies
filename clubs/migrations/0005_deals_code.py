# Generated by Django 2.2.1 on 2019-08-11 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0004_auto_20190811_1118'),
    ]

    operations = [
        migrations.AddField(
            model_name='deals',
            name='code',
            field=models.CharField(default='', max_length=15),
        ),
    ]
