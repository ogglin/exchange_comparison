# Generated by Django 3.1 on 2021-01-18 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotbit_module', '0003_auto_20210116_1601'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotbit',
            name='contract',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='hotbit',
            name='decimals',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
