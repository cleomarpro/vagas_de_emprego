# Generated by Django 4.0.4 on 2022-08-09 20:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recrutador', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vaga',
            old_name='faixa_salarial',
            new_name='pretencao_salarial',
        ),
    ]