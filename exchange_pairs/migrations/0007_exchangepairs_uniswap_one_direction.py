# Generated by Django 3.1 on 2020-08-27 10:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('uniswap_module', '0004_uniswapone'),
        ('exchange_pairs', '0006_auto_20200824_1213'),
    ]

    operations = [
        migrations.AddField(
            model_name='exchangepairs',
            name='uniswap_one_direction',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='uniswap_module.uniswapone'),
        ),
    ]