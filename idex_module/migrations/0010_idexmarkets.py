# Generated by Django 3.1 on 2021-04-06 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idex_module', '0009_idexsocketlog_log'),
    ]

    operations = [
        migrations.CreateModel(
            name='IdexMarkets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('market', models.CharField(max_length=30, unique=True)),
                ('token', models.CharField(blank=True, max_length=30, null=True)),
                ('tsymbol', models.CharField(blank=True, max_length=100, null=True)),
                ('is_active', models.BooleanField(verbose_name='Активный')),
            ],
            options={
                'db_table': 'idex_markets',
            },
        ),
    ]
