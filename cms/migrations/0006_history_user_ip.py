# Generated by Django 5.0.3 on 2024-04-04 02:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cms", "0005_history"),
    ]

    operations = [
        migrations.AddField(
            model_name="history",
            name="user_ip",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
