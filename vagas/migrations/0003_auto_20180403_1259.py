# Generated by Django 2.0.2 on 2018-04-03 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vagas', '0002_vaga_inscritos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vaga',
            name='inscritos',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Quantidade de inscritos'),
        ),
    ]