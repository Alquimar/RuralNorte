# Generated by Django 2.0.4 on 2018-04-27 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0055_auto_20180427_1710'),
    ]

    operations = [
        migrations.AddField(
            model_name='lote',
            name='necessita_licenciamento_ambiental',
            field=models.IntegerField(default=0, verbose_name='Necessita de licenciamento ambiental de atividade?'),
        ),
    ]
