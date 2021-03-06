# Generated by Django 3.1 on 2020-09-16 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exchange_pairs', '0013_settingsmodules'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='settingsmodules',
            options={'verbose_name': 'Настройка модуля', 'verbose_name_plural': 'Настройки модулей'},
        ),
        migrations.AddField(
            model_name='settings',
            name='freeze_percent',
            field=models.FloatField(default=1, help_text='в %', verbose_name='Процент заморозки '),
        ),
    ]
