# Generated by Django 3.2.9 on 2021-11-30 16:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simple', '0011_copies'),
    ]

    operations = [
        migrations.RenameField(
            model_name='copies',
            old_name='size',
            new_name='sizeCp',
        ),
        migrations.RenameField(
            model_name='copies',
            old_name='stock',
            new_name='stockCp',
        ),
    ]