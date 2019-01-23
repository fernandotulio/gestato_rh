# Generated by Django 2.1 on 2018-12-25 20:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('funcionarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=100)),
                ('arquivo', models.FileField(upload_to='documentos')),
                ('pertence', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='funcionarios.Funcionario')),
            ],
        ),
    ]
