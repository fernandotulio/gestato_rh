# Generated by Django 2.1.1 on 2019-02-10 18:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enderecos', '0004_auto_20190210_1633'),
    ]

    operations = [
        migrations.RenameField(
            model_name='endereco',
            old_name='sexo',
            new_name='tipo_endereco',
        ),
    ]
