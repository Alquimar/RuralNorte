# Generated by Django 2.0.5 on 2018-08-13 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aplicacaocredito',
            name='valor',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='Valor (R$)'),
        ),
        migrations.AlterField(
            model_name='creditobancario',
            name='valor',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='Valor (R$)'),
        ),
    ]