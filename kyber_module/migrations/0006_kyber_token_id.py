# Generated by Django 3.1 on 2021-02-03 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kyber_module', '0005_kyber_volume'),
    ]

    operations = [
        migrations.AddField(
            model_name='kyber',
            name='token_id',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]