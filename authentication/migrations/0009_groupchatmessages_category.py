# Generated by Django 4.2.10 on 2024-07-15 19:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("shop", "0001_initial"),
        ("authentication", "0008_groupchatmessages"),
    ]

    operations = [
        migrations.AddField(
            model_name="groupchatmessages",
            name="category",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="shop.category",
            ),
        ),
    ]
