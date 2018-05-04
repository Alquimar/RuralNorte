# Generated by Django 2.0.4 on 2018-05-03 04:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0065_lote_oferta_transporte_interno'),
    ]

    operations = [
        migrations.CreateModel(
            name='DescarteAnimal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_criacao', models.IntegerField(verbose_name='Tipo de criação')),
                ('especificacao', models.IntegerField(choices=[(10, 'Touros'), (20, 'Vacas'), (30, 'Novilhas(os) + de 02 anos'), (40, 'Novilhas(os) + de 01 ano'), (50, 'Bezerras(os)'), (60, 'Boi')], verbose_name='Especificação')),
                ('quantidade_cabecas_consumo', models.IntegerField(verbose_name='Nº de Cabeça(s) - Consumo')),
                ('quantidade_cabecas_comercio', models.IntegerField(verbose_name='Nº de Cabeça(s) - Comércio')),
                ('valor_cabeca', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='R$/Cabeça')),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('atualizado_em', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('lote', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='descartesAnimais', to='core.Lote', verbose_name='Lote')),
            ],
        ),
        migrations.RenameField(
            model_name='producaoanimal',
            old_name='quantidade_cabeças',
            new_name='quantidade_cabecas',
        ),
        migrations.CreateModel(
            name='BovinoculturaCorte',
            fields=[
            ],
            options={
                'verbose_name': 'Descarte Animal - Bovinocultura de Corte',
                'verbose_name_plural': 'Descarte Animal - Bovinocultura de Corte',
                'proxy': True,
                'indexes': [],
            },
            bases=('core.descarteanimal',),
        ),
        migrations.CreateModel(
            name='BovinoculturaLeiteira',
            fields=[
            ],
            options={
                'verbose_name': 'Descarte Animal - Bovinocultura Leiteira',
                'verbose_name_plural': 'Descarte Animal - Bovinocultura Leiteira',
                'proxy': True,
                'indexes': [],
            },
            bases=('core.descarteanimal',),
        ),
    ]
