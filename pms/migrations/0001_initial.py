# Generated by Django 5.0.3 on 2024-04-02 08:50

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Room",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                ("floor", models.CharField(blank=True, max_length=10, null=True)),
                ("room_number", models.CharField(blank=True, max_length=20, null=True)),
                ("type", models.CharField(blank=True, max_length=20, null=True)),
                ("status", models.CharField(blank=True, max_length=20, null=True)),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
