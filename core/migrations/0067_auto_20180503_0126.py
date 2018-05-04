# Generated by Django 2.0.4 on 2018-05-03 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0066_auto_20180503_0121'),
    ]

    operations = [
        migrations.AddField(
            model_name='descarteanimal',
            name='canal_comercializacao',
            field=models.IntegerField(choices=[(1, 'Venda para outro produtor'), (2, 'Entrega para frigorífico/açougue'), (3, 'Venda para agentes "atravessadores"'), (4, 'Outros')], default=0, verbose_name='Formas/Canais de Comercialização'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='descarteanimal',
            name='canal_comercializacao_outros',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Outros (Especificar)'),
        ),
    ]
