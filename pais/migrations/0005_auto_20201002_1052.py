# Generated by Django 3.0.2 on 2020-10-02 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pais', '0004_religiao_descricao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pais',
            name='capital',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='pais',
            name='capital_sigla',
            field=models.CharField(default='', max_length=5),
        ),
        migrations.AlterField(
            model_name='pais',
            name='populacao',
            field=models.CharField(default='', max_length=50),
        ),
    ]