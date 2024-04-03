# Generated by Django 5.0.3 on 2024-04-03 06:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pms", "0008_checkinoutstatus_delete_checkin"),
    ]

    operations = [
        migrations.AddField(
            model_name="reservation",
            name="m_i_a",
            field=models.CharField(
                blank=True,
                choices=[("m", "M"), ("i", "I"), ("a", "A")],
                max_length=3,
                null=True,
            ),
        ),
    ]