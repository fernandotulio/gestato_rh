# Generated by Django 2.1.1 on 2019-02-10 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enderecos', '0006_auto_20190210_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endereco',
            name='tipo_endereco',
            field=models.CharField(choices=[('COMERCIAL', 'COMERCIAL'), ('RESIDENCIAL', 'RESIDENCIAL')], default='RESIDENCIAL', max_length=2),
        ),
    ]
