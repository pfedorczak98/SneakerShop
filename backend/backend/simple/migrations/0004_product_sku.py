# Generated by Django 3.2.9 on 2021-11-28 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simple', '0003_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sku',
            field=models.IntegerField(default=0),
        ),
    ]
