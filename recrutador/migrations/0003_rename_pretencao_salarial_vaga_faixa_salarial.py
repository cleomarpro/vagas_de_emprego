# Generated by Django 4.0.4 on 2022-08-09 20:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recrutador', '0002_rename_faixa_salarial_vaga_pretencao_salarial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vaga',
            old_name='pretencao_salarial',
            new_name='faixa_salarial',
        ),
    ]
