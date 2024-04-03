# Generated by Django 5.0.3 on 2024-04-03 04:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pms", "0005_remove_reservation_room_reservation_room_number_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="CheckIn",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("check_in_time", models.TimeField(blank=True, null=True)),
                (
                    "reservation",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="check_in",
                        to="pms.reservation",
                    ),
                ),
            ],
        ),
    ]