# Generated by Django 3.1 on 2020-08-27 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uniswap_module', '0005_auto_20200827_1345'),
    ]

    operations = [
        migrations.AddField(
            model_name='uniswap',
            name='tokenid',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='uniswapone',
            name='tokenid',
            field=models.CharField(default='', max_length=500),
        ),
    ]
