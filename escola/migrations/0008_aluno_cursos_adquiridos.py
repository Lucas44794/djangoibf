# Generated by Django 5.1 on 2024-08-31 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0007_alter_modulos_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='cursos_adquiridos',
            field=models.ManyToManyField(blank=True, related_name='alunos', to='escola.cursos'),
        ),
    ]
