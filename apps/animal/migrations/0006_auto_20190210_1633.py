# Generated by Django 2.1.1 on 2019-02-10 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animal', '0005_animal_sexo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='sexo',
            field=models.CharField(choices=[('M', 'MACHO'), ('F', 'FEMEA')], default='M', max_length=2),
        ),
    ]
