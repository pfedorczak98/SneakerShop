# Generated by Django 3.2.9 on 2021-12-02 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simple', '0015_alter_copies__id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='size',
        ),
        migrations.RemoveField(
            model_name='product',
            name='stock',
        ),
    ]
