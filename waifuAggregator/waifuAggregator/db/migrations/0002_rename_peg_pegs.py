# Generated by Django 4.0.4 on 2022-05-25 20:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='peg',
            new_name='pegs',
        ),
    ]