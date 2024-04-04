# Generated by Django 5.0.3 on 2024-04-04 01:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cms", "0004_cmsreservation_channel"),
    ]

    operations = [
        migrations.CreateModel(
            name="History",
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
                ("user_name", models.CharField(blank=True, max_length=20, null=True)),
                ("connection_date", models.DateTimeField(auto_now=True)),
                (
                    "program_name",
                    models.CharField(blank=True, max_length=20, null=True),
                ),
                ("process", models.CharField(blank=True, max_length=20, null=True)),
                (
                    "process_content",
                    models.CharField(blank=True, max_length=20, null=True),
                ),
                ("user_id", models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
    ]