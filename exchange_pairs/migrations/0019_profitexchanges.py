# Generated by Django 3.1 on 2021-01-25 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exchange_pairs', '0018_auto_20210120_1426'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfitExchanges',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pair', models.CharField(max_length=100)),
                ('buy_name', models.CharField(max_length=100)),
                ('buy', models.FloatField()),
                ('sell_name', models.CharField(max_length=100)),
                ('sell', models.FloatField()),
                ('percent', models.FloatField()),
                ('tokenid', models.CharField(max_length=100)),
                ('buyurl', models.CharField(max_length=200)),
                ('sellurl', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Выгодные обмены',
                'verbose_name_plural': 'Выгодный обмен',
                'db_table': 'profit_exchanges',
            },
        ),
    ]