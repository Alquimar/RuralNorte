# Generated by Django 2.0.5 on 2018-08-21 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20180820_0039'),
    ]

    operations = [
        migrations.AddField(
            model_name='membro',
            name='codigo_familia',
            field=models.IntegerField(blank=True, null=True, verbose_name='Código da Família'),
        ),
    ]
