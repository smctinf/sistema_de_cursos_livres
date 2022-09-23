# Generated by Django 3.2.15 on 2022-09-23 18:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0008_responsavel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='responsavel',
            old_name='bairro',
            new_name='r_bairro',
        ),
        migrations.RenameField(
            model_name='responsavel',
            old_name='celular',
            new_name='r_celular',
        ),
        migrations.RenameField(
            model_name='responsavel',
            old_name='cep',
            new_name='r_cep',
        ),
        migrations.RenameField(
            model_name='responsavel',
            old_name='cpf',
            new_name='r_cpf',
        ),
        migrations.RenameField(
            model_name='responsavel',
            old_name='dt_nascimento',
            new_name='r_dt_nascimento',
        ),
        migrations.RenameField(
            model_name='responsavel',
            old_name='email',
            new_name='r_email',
        ),
        migrations.RenameField(
            model_name='responsavel',
            old_name='endereco',
            new_name='r_endereco',
        ),
        migrations.RenameField(
            model_name='responsavel',
            old_name='estado_civil',
            new_name='r_estado_civil',
        ),
        migrations.RenameField(
            model_name='responsavel',
            old_name='nome',
            new_name='r_nome',
        ),
        migrations.RenameField(
            model_name='responsavel',
            old_name='profissão',
            new_name='r_profissão',
        ),
        migrations.RenameField(
            model_name='responsavel',
            old_name='rg',
            new_name='r_rg',
        ),
        migrations.RenameField(
            model_name='responsavel',
            old_name='sexo',
            new_name='r_sexo',
        ),
        migrations.RemoveField(
            model_name='responsavel',
            name='aluno',
        ),
        migrations.AddField(
            model_name='responsavel',
            name='r_aluno',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cursos.aluno'),
        ),
    ]
