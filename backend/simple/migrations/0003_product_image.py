# Generated by Django 3.2.9 on 2021-11-22 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simple', '0002_auto_20211122_2219'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]