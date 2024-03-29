# Generated by Django 2.0.2 on 2018-04-02 13:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(max_length=14, unique=True, verbose_name='CPF')),
                ('data_nascimento', models.DateField(blank=True, null=True, verbose_name='Data de Nascimento')),
                ('logradouro', models.CharField(blank=True, max_length=100, null=True, verbose_name='Rua')),
                ('numeroLog', models.CharField(blank=True, max_length=10, null=True, verbose_name='Número')),
                ('bairro', models.CharField(blank=True, max_length=50, null=True, verbose_name='Bairro')),
                ('cidade', models.CharField(blank=True, max_length=50, null=True, verbose_name='Cidade')),
                ('uf', models.CharField(blank=True, max_length=50, null=True, verbose_name='UF')),
                ('cep', models.CharField(blank=True, max_length=10, null=True, verbose_name='CEP')),
                ('complemento', models.CharField(blank=True, max_length=100, null=True, verbose_name='Complemento')),
                ('tel1', models.CharField(blank=True, max_length=12, null=True, verbose_name='Tel(1)')),
                ('tel2', models.CharField(blank=True, max_length=12, null=True, verbose_name='Tel(2)')),
                ('obs', models.CharField(blank=True, max_length=200, null=True)),
                ('deficiente', models.CharField(blank=True, choices=[('', ''), ('Sim', 'Sim'), ('Nao', 'Não')], max_length=5, null=True, verbose_name='Portador de deficiência')),
                ('escolaridade', models.CharField(blank=True, choices=[('', ''), ('Fundamental incompleto', 'Fundamental incompleto'), ('Fundamental completo', 'Fundamental completo'), ('Medio incompleto', 'Médio incompleto'), ('Medio completo', 'Médio completo'), ('Tecnico incompleto', 'Técnico incompleto'), ('Tecnico completo', 'Técnico completo'), ('Superior incompleto', 'Superior incompleto'), ('Superior completo', 'Superior completo'), ('Pos-Graduacao', 'Pós-Graduação'), ('Mestrado', 'Mestrado'), ('Doutorado', 'Doutorado'), ('PHD', 'PHD')], max_length=25, null=True, verbose_name='Escolaridade')),
                ('habilitacao', models.CharField(blank=True, choices=[('', ''), ('A', 'A'), ('AB', 'AB'), ('AC', 'AC'), ('AD', 'AD'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=25, null=True, verbose_name='Habilitação')),
                ('estado_civil', models.CharField(blank=True, choices=[('', ''), ('Solteiro', 'Solteiro(a)'), ('Casado', 'Casado(a)'), ('Divorciado', 'Divorciado(a)'), ('Outros', 'Outros')], max_length=25, null=True, verbose_name='Estado civil')),
                ('genero', models.CharField(blank=True, choices=[('', ''), ('Masculino', 'Masculino'), ('Feminino', 'Feminino'), ('Outros', 'Outros')], max_length=25, null=True, verbose_name='Gênero')),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(blank=True, choices=[('', ''), ('Curso de Qualificacao', 'Curso de Qualificação'), ('Curso Profissionalizante', 'Curso Profissionalizante'), ('Palestra', 'Palestra'), ('Simposio', 'Simpósio')], max_length=25, null=True, verbose_name='Tipo')),
                ('curso', models.CharField(blank=True, max_length=50, null=True, verbose_name='Curso')),
                ('instituicao', models.CharField(blank=True, max_length=30, null=True, verbose_name='Instituição')),
                ('duracao', models.CharField(blank=True, max_length=5, null=True, verbose_name='Duração')),
                ('data_entrada', models.DateField(blank=True, null=True, verbose_name='Data de Entrada')),
                ('data_saida', models.DateField(blank=True, null=True, verbose_name='Data de Conclusão')),
                ('candidato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='candidato.Candidato')),
            ],
        ),
        migrations.CreateModel(
            name='Experiencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empresa', models.CharField(blank=True, max_length=100, null=True, verbose_name='Empresa')),
                ('cargo', models.CharField(blank=True, max_length=100, null=True, verbose_name='Cargo')),
                ('descricao', models.TextField(blank=True, max_length=1000, null=True, verbose_name='Descrição das atividades')),
                ('data_entrada', models.DateField(blank=True, null=True, verbose_name='Data da contratação')),
                ('data_saida', models.DateField(blank=True, null=True, verbose_name='Data da saída')),
                ('candidato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='candidato.Candidato')),
            ],
        ),
        migrations.CreateModel(
            name='Formacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grau', models.CharField(blank=True, choices=[('', ''), ('Medio Tecnico', 'Médio Técnico'), ('Superior', 'Superior'), ('Especializacao', 'Especialização'), ('Pos-Graduacao', 'Pós-Graduação'), ('Mestrado', 'Mestrado'), ('Doutorado', 'Doutorado'), ('PHD', 'PHD')], max_length=25, null=True, verbose_name='Nível')),
                ('instituicao', models.CharField(blank=True, max_length=100, null=True, verbose_name='Instituição')),
                ('curso', models.CharField(blank=True, max_length=50, null=True, verbose_name='Curso')),
                ('data_entrada', models.DateField(blank=True, null=True, verbose_name='Data de Entrada')),
                ('data_conclusao', models.DateField(blank=True, null=True, verbose_name='Data de Saída')),
                ('candidato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='formacao', to='candidato.Candidato')),
            ],
        ),
        migrations.CreateModel(
            name='Idioma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idioma', models.CharField(blank=True, max_length=20, null=True)),
                ('nivel', models.CharField(blank=True, choices=[('', ''), ('Basico', 'Básico'), ('Intermediario', 'Intermediário'), ('Avancado', 'Avançado'), ('Fluente', 'Fluente')], max_length=25, null=True)),
                ('candidato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='candidato.Candidato')),
            ],
        ),
        migrations.CreateModel(
            name='Pretencoes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('experiencia', models.BooleanField(default=False, verbose_name='Tenho experiência na função')),
                ('comprovacao', models.BooleanField(default=False, verbose_name='Posso comprovar')),
                ('candidato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='candidato.Candidato')),
            ],
        ),
        migrations.CreateModel(
            name='Profissoes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_prof', models.CharField(blank=True, max_length=100, null=True, verbose_name='Profissão')),
            ],
        ),
        migrations.AddField(
            model_name='pretencoes',
            name='profissao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='candidato.Profissoes'),
        ),
    ]
