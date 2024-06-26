# Generated by Django 5.0.3 on 2024-04-03 07:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pms", "0009_reservation_m_i_a"),
    ]

    operations = [
        migrations.AddField(
            model_name="reservation",
            name="booker_number",
            field=models.CharField(
                blank=True,
                choices=[("m", "M"), ("i", "I"), ("a", "A")],
                max_length=20,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="reservation",
            name="cancellation_date",
            field=models.CharField(
                blank=True,
                choices=[("m", "M"), ("i", "I"), ("a", "A")],
                max_length=20,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="reservation",
            name="deposit_amount",
            field=models.DecimalField(decimal_places=0, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name="reservation",
            name="deposit_number",
            field=models.CharField(
                blank=True,
                choices=[("m", "M"), ("i", "I"), ("a", "A")],
                max_length=20,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="reservation",
            name="guest_count",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="reservation",
            name="ota_number",
            field=models.CharField(
                blank=True,
                choices=[("m", "M"), ("i", "I"), ("a", "A")],
                max_length=20,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="reservation",
            name="reservation_date",
            field=models.CharField(
                blank=True,
                choices=[("m", "M"), ("i", "I"), ("a", "A")],
                max_length=20,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="reservation",
            name="reservation_number",
            field=models.CharField(
                blank=True,
                choices=[("m", "M"), ("i", "I"), ("a", "A")],
                max_length=20,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="reservation",
            name="reservation_path",
            field=models.CharField(
                blank=True,
                choices=[("m", "M"), ("i", "I"), ("a", "A")],
                max_length=20,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="reservation",
            name="reservation_status",
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name="reservation",
            name="room_count",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="reservation",
            name="sales_person",
            field=models.CharField(
                blank=True,
                choices=[("m", "M"), ("i", "I"), ("a", "A")],
                max_length=20,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="reservation",
            name="vehicle_number",
            field=models.CharField(
                blank=True,
                choices=[("m", "M"), ("i", "I"), ("a", "A")],
                max_length=20,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="reservation",
            name="verifier",
            field=models.CharField(
                blank=True,
                choices=[("m", "M"), ("i", "I"), ("a", "A")],
                max_length=20,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="reservation",
            name="vip_guest",
            field=models.CharField(
                blank=True,
                choices=[("m", "M"), ("i", "I"), ("a", "A")],
                max_length=20,
                null=True,
            ),
        ),
        migrations.RemoveField(
            model_name="reservation",
            name="room",
        ),
        migrations.AlterField(
            model_name="reservation",
            name="services",
            field=models.DecimalField(decimal_places=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name="reservation",
            name="total_room_charge",
            field=models.DecimalField(decimal_places=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name="room",
            name="price",
            field=models.DecimalField(decimal_places=0, max_digits=10),
        ),
        migrations.AddField(
            model_name="reservation",
            name="room",
            field=models.ManyToManyField(
                blank=True, related_name="reservations", to="pms.room"
            ),
        ),
    ]
