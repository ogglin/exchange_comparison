# Generated by Django 3.1 on 2020-09-03 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exchange_pairs', '0011_auto_20200903_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comparepairs',
            name='decimals',
            field=models.IntegerField(null=True),
        ),
    ]
