# Generated by Django 4.0.4 on 2022-08-10 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidato', '0004_dadospessoais_remove_minhaiscricao_pretecao_salarial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dadospessoais',
            name='pretecao_salarial',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='dadospessoais',
            name='telefone',
            field=models.CharField(max_length=50, null=True),
        ),
    ]