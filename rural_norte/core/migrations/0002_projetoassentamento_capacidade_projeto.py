# Generated by Django 2.0.5 on 2018-05-23 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projetoassentamento',
            name='capacidade_projeto',
            field=models.IntegerField(default=0, verbose_name='Capacidade do Projeto'),
            preserve_default=False,
        ),
    ]