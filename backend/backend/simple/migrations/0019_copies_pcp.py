# Generated by Django 3.2.9 on 2021-12-02 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simple', '0018_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='copies',
            name='pCp',
            field=models.DecimalField(blank=True, decimal_places=1, default=0, max_digits=5),
        ),
    ]