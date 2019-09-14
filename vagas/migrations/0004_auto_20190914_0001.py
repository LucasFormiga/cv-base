# Generated by Django 2.2.5 on 2019-09-14 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vagas', '0003_candidatura_vaga'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidatura',
            name='vaga',
            field=models.CharField(choices=[('DEVELOP', 'Develop'), ('GERENTE_PROJETO', 'GerenteProjeto'), ('MARKETING', 'Marketing'), ('UXDESIGNER', 'UXDesigner'), ('DESIGNER', 'Designer')], default='DEVELOP', max_length=100),
        ),
    ]