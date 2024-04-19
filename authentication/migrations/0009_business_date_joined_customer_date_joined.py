# Generated by Django 5.0 on 2024-04-19 15:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("authentication", "0008_business_verified_customer_verified"),
    ]

    operations = [
        migrations.AddField(
            model_name="business",
            name="date_joined",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name="customer",
            name="date_joined",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
