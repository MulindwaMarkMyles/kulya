# Generated by Django 5.0.1 on 2024-03-09 10:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shop", "0003_alter_product_owner"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
    ]
