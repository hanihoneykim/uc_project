# Generated by Django 5.0.3 on 2024-04-03 02:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pms", "0002_reservation_room_reservation"),
    ]

    operations = [
        migrations.AlterField(
            model_name="reservation",
            name="length_of_stay",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="reservation",
            name="remarks",
            field=models.TextField(blank=True, null=True),
        ),
    ]
