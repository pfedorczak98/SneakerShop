# Generated by Django 3.2.9 on 2021-12-09 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simple', '0026_auto_20211209_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='copies',
            name='stockCp',
            field=models.IntegerField(default=0),
        ),
    ]
