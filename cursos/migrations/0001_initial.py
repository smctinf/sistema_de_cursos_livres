# Generated by Django 3.2.15 on 2022-09-09 13:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150, verbose_name='Nome completo do aluno')),
                ('celular', models.CharField(max_length=12, verbose_name='Celular p/ contato do aluno')),
                ('email', models.EmailField(max_length=254, verbose_name='Email p/ contato do aluno')),
                ('dt_nascimento', models.DateField(verbose_name='Data de Nascimento do aluno')),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], max_length=1, verbose_name='Qual foi o sexo atribuído no nascimento?')),
                ('endereco', models.CharField(max_length=150, null=True, verbose_name='Endereço do aluno')),
                ('bairro', models.CharField(max_length=80, null=True)),
                ('cpf', models.CharField(max_length=150, verbose_name='CPF')),
                ('dt_inclusao', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150, verbose_name='Nome da categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('carga_horaria', models.CharField(max_length=150)),
                ('descricao', models.TextField(default='')),
                ('ativo', models.BooleanField(default=True)),
                ('dt_inclusao', models.DateField(auto_now_add=True)),
                ('dt_alteracao', models.DateField(auto_now=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cursos.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Instituicao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Local',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150, verbose_name='Nome do local')),
                ('endereco', models.CharField(max_length=150, verbose_name='Endereço')),
                ('bairro', models.CharField(max_length=80, verbose_name='Endereço')),
                ('cep', models.CharField(max_length=9, verbose_name='CEP')),
                ('ativo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150, verbose_name='Nome completo do aluno')),
                ('celular', models.CharField(max_length=12, verbose_name='Celular p/ contato do aluno')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Email p/ contato do aluno')),
                ('endereco', models.CharField(blank=True, max_length=150, null=True, verbose_name='Endereço do aluno')),
                ('bairro', models.CharField(blank=True, max_length=80, null=True)),
                ('cpf', models.CharField(max_length=150, verbose_name='CPF')),
                ('dt_inclusao', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horario', models.CharField(max_length=150)),
                ('qnt', models.IntegerField(verbose_name='Quantidade de alunos permitidos')),
                ('data_inicio', models.DateField()),
                ('data_final', models.DateField()),
                ('dt_inclusao', models.DateField(auto_now_add=True)),
                ('dt_alteracao', models.DateField(auto_now=True)),
                ('status', models.CharField(choices=[('pre', 'Pré-inscrição'), ('agu', 'Aguardando'), ('ati', 'Ativa'), ('acc', 'Ativa e aceitando candidatos'), ('enc', 'Encerrada')], default='pre', max_length=3, verbose_name='Qual o status da turma?')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cursos.curso', verbose_name='Atividade')),
                ('instrutor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cursos.professor')),
                ('local', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cursos.local')),
                ('user_inclusao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='TurmaUserInclusao', to=settings.AUTH_USER_MODEL)),
                ('user_ultima_alteracao', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='TurmaUserAlteracao', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_matricula', models.DateField(auto_now_add=True)),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cursos.aluno')),
                ('turma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cursos.turma')),
            ],
        ),
        migrations.AddField(
            model_name='curso',
            name='instituicao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cursos.instituicao'),
        ),
        migrations.AddField(
            model_name='curso',
            name='user_inclusao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userInclusao', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='curso',
            name='user_ultima_alteracao',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='userAlteracao', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Candidato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150, verbose_name='Nome completo do candidato')),
                ('celular', models.CharField(max_length=12, verbose_name='Celular p/ contato do candidato')),
                ('email', models.EmailField(max_length=254, verbose_name='Email p/ contato do candidato')),
                ('dt_nascimento', models.DateField(verbose_name='Data de Nascimento')),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], max_length=1, verbose_name='Qual foi o sexo atribuído no seu nascimento?')),
                ('cep', models.CharField(max_length=9, verbose_name='CEP')),
                ('endereco', models.CharField(max_length=150, null=True, verbose_name='Endereço do candidato')),
                ('bairro', models.CharField(max_length=80, null=True)),
                ('cpf', models.CharField(max_length=150, verbose_name='CPF')),
                ('rg', models.CharField(blank=True, max_length=9, verbose_name='RG')),
                ('nome_da_mãe', models.CharField(max_length=150, verbose_name='Nome completo da mãe do candidato')),
                ('aceita_mais_informacoes', models.BooleanField(verbose_name='Declaro que aceito receber email com as informações das atividades')),
                ('dt_inclusao', models.DateField(auto_now_add=True)),
                ('turmas', models.ManyToManyField(to='cursos.Turma')),
                ('turmas_selecionado', models.ManyToManyField(blank=True, null=True, related_name='tselecionado', to='cursos.Turma')),
            ],
        ),
    ]
