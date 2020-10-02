# Generated by Django 3.0.2 on 2020-10-02 12:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Continente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(db_index=True, max_length=100, unique=True)),
            ],
            options={
                'db_table': 'continente',
                'ordering': ('nome',),
            },
        ),
        migrations.CreateModel(
            name='Idioma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(db_index=True, max_length=100, unique=True)),
            ],
            options={
                'db_table': 'idioma',
                'ordering': ('nome',),
            },
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(db_index=True, max_length=100, unique=True)),
                ('sigla', models.CharField(db_index=True, max_length=5, unique=True)),
                ('populacao', models.CharField(db_index=True, max_length=50, unique=True)),
                ('capital', models.CharField(db_index=True, max_length=100, unique=True)),
                ('capital_sigla', models.CharField(db_index=True, max_length=5, unique=True)),
                ('clima', models.TextField(blank=True)),
                ('cristaos', models.TextField(blank=True)),
                ('curiosidades', models.TextField(blank=True)),
                ('historia', models.TextField(blank=True)),
                ('continente', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='pais.Continente')),
            ],
            options={
                'db_table': 'pais',
                'ordering': ('nome',),
            },
        ),
        migrations.CreateModel(
            name='Perseguicao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.TextField(blank=True)),
                ('descricao', models.TextField(blank=True)),
            ],
            options={
                'db_table': 'perseguicao',
            },
        ),
        migrations.CreateModel(
            name='Religiao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(db_index=True, max_length=100, unique=True)),
            ],
            options={
                'db_table': 'religiao',
                'ordering': ('nome',),
            },
        ),
        migrations.CreateModel(
            name='Turismo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('decricao', models.TextField(blank=True)),
                ('imagem', models.ImageField(upload_to='images/turismo/')),
                ('pais', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='pais.Pais')),
            ],
            options={
                'db_table': 'turismo',
            },
        ),
        migrations.CreateModel(
            name='PaisReligiao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pais', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='pais.Pais')),
                ('religiao', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='pais.Religiao')),
            ],
            options={
                'db_table': 'pais_religiao',
            },
        ),
        migrations.CreateModel(
            name='PaisIdioma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idioma', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='pais.Idioma')),
                ('pais', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='pais.Pais')),
            ],
            options={
                'db_table': 'pais_idioma',
            },
        ),
        migrations.AddField(
            model_name='pais',
            name='perseguido',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='pais.Perseguicao'),
        ),
    ]