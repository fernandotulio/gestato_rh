# Generated by Django 2.1.1 on 2019-02-17 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servico', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='servico',
            old_name='pertence',
            new_name='id_animal',
        ),
    ]
