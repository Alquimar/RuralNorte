# Generated by Django 2.0.4 on 2018-04-30 19:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0062_auto_20180430_1621'),
    ]

    operations = [
        migrations.CreateModel(
            name='EspacoDisponivel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('espaco_disponivel', models.IntegerField(choices=[(1, 'Quadra de esportes'), (2, 'Campo de futebol'), (3, 'Salão de festas'), (4, 'Não possui')], verbose_name='Esporte/atividade física')),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('atualizado_em', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('lote', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='espacosDisponiveis', to='core.Lote', verbose_name='Lote')),
            ],
            options={
                'verbose_name': 'Espaço disponível para a prática de esporte/recreação',
                'verbose_name_plural': 'No assentamento quais são os espaços disponíveis para a prática de esporte ou para a recreação?',
            },
        ),
    ]
