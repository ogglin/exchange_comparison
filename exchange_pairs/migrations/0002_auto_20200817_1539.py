# Generated by Django 3.1 on 2020-08-17 12:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bancor_module', '0002_auto_20200816_1422'),
        ('uniswap_module', '0002_auto_20200816_1422'),
        ('idex_module', '0003_auto_20200816_1422'),
        ('kyber_module', '0002_auto_20200816_1422'),
        ('exchange_pairs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exchangepairs',
            name='bancor_direction',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='bancor_module.bancor'),
        ),
        migrations.AlterField(
            model_name='exchangepairs',
            name='idex_direction',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='idex_module.idex'),
        ),
        migrations.AlterField(
            model_name='exchangepairs',
            name='kyber_direction',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='kyber_module.kyber'),
        ),
        migrations.AlterField(
            model_name='exchangepairs',
            name='uniswap_direction',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='uniswap_module.uniswap'),
        ),
    ]
