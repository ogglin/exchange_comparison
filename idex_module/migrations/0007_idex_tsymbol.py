# Generated by Django 3.1 on 2021-02-20 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idex_module', '0006_auto_20210203_2213'),
    ]

    operations = [
        migrations.AddField(
            model_name='idex',
            name='tsymbol',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
