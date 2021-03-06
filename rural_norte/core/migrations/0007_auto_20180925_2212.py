# Generated by Django 2.0.5 on 2018-09-26 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20180821_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membro',
            name='opcao_ensino_utilizada',
            field=models.IntegerField(blank=True, choices=[(10, 'Frequenta escola em outro assentamento'), (20, 'Frequenta escola na cidade mais próxima'), (30, 'Deixa de frequentar a escola'), (99, 'Outros'), (199, 'Não se aplica')], null=True, verbose_name='Opção de ensino utilizada'),
        ),
        migrations.AlterField(
            model_name='membro',
            name='parentesco',
            field=models.IntegerField(blank=True, choices=[(10, 'Titular'), (20, 'Cônjuge'), (24, 'Pai'), (28, 'Mãe'), (30, 'Irmão(a)'), (40, 'Tio(a)'), (45, 'Sobrinho(a)'), (50, 'Primo(a)'), (60, 'Filho(a)'), (70, 'Enteado(a)'), (80, 'Cunhado(a)'), (90, 'Genro/Nora'), (100, 'Neto(a)'), (110, 'Agregado(a)')], null=True, verbose_name='Parentesco'),
        ),
    ]
