# Generated by Django 2.2.1 on 2019-08-11 18:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0005_deals_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deals',
            name='club',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clubs.Club'),
        ),
    ]
