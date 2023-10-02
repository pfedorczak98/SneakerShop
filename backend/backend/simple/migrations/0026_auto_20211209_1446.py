# Generated by Django 3.2.9 on 2021-12-09 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simple', '0025_remove_product_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='copies',
            name='sizeCp',
            field=models.DecimalField(decimal_places=1, max_digits=5),
        ),
        migrations.AlterField(
            model_name='copies',
            name='stockCp',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
