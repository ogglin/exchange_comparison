# Generated by Django 3.1 on 2021-02-20 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uniswap_module', '0008_auto_20210203_2102'),
    ]

    operations = [
        migrations.AddField(
            model_name='uniswap',
            name='tsymbol',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='uniswapone',
            name='tsymbol',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
