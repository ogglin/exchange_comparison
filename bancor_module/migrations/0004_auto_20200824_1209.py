# Generated by Django 3.1 on 2020-08-24 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bancor_module', '0003_bancor_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bancor',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Активный'),
        ),
    ]