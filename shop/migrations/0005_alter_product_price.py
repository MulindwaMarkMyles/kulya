# Generated by Django 5.0.1 on 2024-03-10 08:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shop", "0004_product_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="price",
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
    ]
