# Generated by Django 2.0.4 on 2018-04-25 22:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_auto_20180425_1926'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lote',
            old_name='utilizacao_mesma_fonte_agua_quantidade',
            new_name='quantidade_familias_utilizacao_mesma_fonte_agua',
        ),
    ]
