# Generated by Django 4.0.4 on 2022-08-17 17:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('candidato', '0002_minhaiscricao_pretencao_salarial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='minhaiscricao',
            name='pretencao_salarial',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='candidato.pretencaosalarial'),
        ),
    ]
