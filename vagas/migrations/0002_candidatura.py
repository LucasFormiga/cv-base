# Generated by Django 2.2.5 on 2019-09-14 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vagas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidatura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('telefone', models.CharField(max_length=255)),
                ('experiencia_profissional', models.TextField(max_length=500)),
                ('experiencia_academica', models.TextField(max_length=500)),
                ('motivacao', models.TextField(max_length=500)),
            ],
        ),
    ]
