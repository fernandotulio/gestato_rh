# Generated by Django 2.1.1 on 2019-01-20 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0005_remove_cliente_endereco'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='celular',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='comercial',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='email',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='imagem',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='observacao',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
