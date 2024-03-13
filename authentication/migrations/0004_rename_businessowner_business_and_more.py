# Generated by Django 5.0.1 on 2024-03-09 09:23

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("authentication", "0003_businessowner_business_name_and_more"),
        ("shop", "0003_alter_product_owner"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name="BusinessOwner",
            new_name="Business",
        ),
        migrations.RenameField(
            model_name="business",
            old_name="user",
            new_name="owner",
        ),
    ]
