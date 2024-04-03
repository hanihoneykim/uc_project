from django.db import models
import uuid


class Room(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, null=False, blank=False)
    floor = models.CharField(max_length=10, null=True, blank=True)
    room_number = models.CharField(max_length=20, null=True, blank=True)
    type = models.CharField(max_length=20, null=True, blank=True)
    status = models.CharField(max_length=20, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    reservation = models.ForeignKey(
        "pms.Reservation", null=True, related_name="room", on_delete=models.CASCADE
    )


class Reservation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, null=False, blank=False)
    group_id = models.CharField(max_length=20, null=True, blank=True)
    guest_name = models.CharField(max_length=30, null=True, blank=True)
    check_in_date = models.DateField(null=True, blank=True)
    check_out_date = models.DateField(null=True, blank=True)
    length_of_stay = models.IntegerField(max_length=10, null=True, blank=True)
    services = models.DecimalField(max_digits=10, decimal_places=2)
    total_room_charge = models.DecimalField(max_digits=10, decimal_places=2)
    vendor_name = models.CharField(max_length=30, null=True, blank=True)
    rate_type = models.CharField(max_length=20, null=True, blank=True)
    market_segment = models.CharField(max_length=20, null=True, blank=True)
    reservation_source = models.CharField(max_length=20, null=True, blank=True)
    package = models.CharField(max_length=20, null=True, blank=True)
    nationality = models.CharField(max_length=20, null=True, blank=True)
    taxes = models.CharField(max_length=10, null=True, blank=True)
    special_services = models.CharField(max_length=50, null=True, blank=True)
    folio_number = models.CharField(max_length=20, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    remarks = models.CharField(max_length=50, null=True, blank=True)
