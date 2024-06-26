# Generated by Django 5.0.3 on 2024-04-05 00:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pms", "0012_task"),
    ]

    operations = [
        migrations.AddField(
            model_name="reservation",
            name="advance_payment",
            field=models.DecimalField(decimal_places=0, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name="reservation",
            name="balance_due",
            field=models.DecimalField(decimal_places=0, max_digits=10, null=True),
        ),
    ]
