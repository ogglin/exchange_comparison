# Generated by Django 3.1 on 2020-08-24 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bancor_module', '0002_auto_20200816_1422'),
    ]

    operations = [
        migrations.AddField(
            model_name='bancor',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]