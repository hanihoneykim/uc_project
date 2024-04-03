# Generated by Django 5.0.3 on 2024-04-03 05:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pms", "0006_checkin"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="reservation",
            name="room_number",
        ),
        migrations.RemoveField(
            model_name="reservation",
            name="room_rate",
        ),
        migrations.RemoveField(
            model_name="reservation",
            name="room_type",
        ),
        migrations.AddField(
            model_name="reservation",
            name="room",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="reservations",
                to="pms.room",
            ),
        ),
    ]
