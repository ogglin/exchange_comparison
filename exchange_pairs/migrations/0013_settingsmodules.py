# Generated by Django 3.1 on 2020-09-12 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exchange_pairs', '0012_auto_20200903_1738'),
    ]

    operations = [
        migrations.CreateModel(
            name='SettingsModules',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('module_name', models.CharField(max_length=200, verbose_name='Модуль')),
                ('is_active', models.BooleanField(verbose_name='Включен')),
            ],
            options={
                'verbose_name': 'Настройка',
                'verbose_name_plural': 'Настройки',
                'db_table': 'settings_modules',
            },
        ),
    ]