# Generated by Django 3.1 on 2021-01-16 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotbit_module', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotbit',
            name='volume',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
