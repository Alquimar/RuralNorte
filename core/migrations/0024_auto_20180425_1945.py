# Generated by Django 2.0.4 on 2018-04-25 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_auto_20180425_1935'),
    ]

    operations = [
        migrations.AddField(
            model_name='lote',
            name='regularidade_abastecimento_agua',
            field=models.IntegerField(choices=[(1, 'Sempre tem água'), (2, 'Fatla água às vezes'), (3, 'Fatla água com frequência'), (4, 'Nunca tem água')], default=0, verbose_name='Regularidade de abastecimento de água'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lote',
            name='situacao_cercado_lote',
            field=models.IntegerField(choices=[(1, 'Totalmente cercado, com divisões internas'), (2, 'Totalmente cercado, sem divisões internas'), (3, 'Parcialmente cercado'), (4, 'Não está cercado')], default=0, verbose_name='Como está cercado o lote?'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lote',
            name='situacao_estrada_acesso',
            field=models.IntegerField(choices=[(1, 'Boa'), (2, 'Razoável'), (3, 'Ruim'), (4, 'Péssima')], default=0, verbose_name='Situação anual da estrada principal acesso ao lote?'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lote',
            name='tipo_estrada_acesso',
            field=models.IntegerField(choices=[(1, 'Asfalto'), (2, 'Estrada cascalhada'), (3, 'Estrada de terra'), (4, 'Trilheiro'), (5, 'Inexistente')], default=0, verbose_name='Como é o acesso ao lote?'),
            preserve_default=False,
        ),
    ]
