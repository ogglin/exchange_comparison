# Generated by Django 3.1 on 2020-10-12 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exchange_pairs', '0014_auto_20200916_1239'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='api_keys',
            field=models.JSONField(blank=True, null=True, verbose_name='API keys'),
        ),
    ]