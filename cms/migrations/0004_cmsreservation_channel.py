# Generated by Django 5.0.3 on 2024-04-04 01:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cms", "0003_cmsreservation"),
    ]

    operations = [
        migrations.AddField(
            model_name="cmsreservation",
            name="channel",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
