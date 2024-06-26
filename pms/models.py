from django.db import models
import uuid


class Room(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, null=False, blank=False)
    floor = models.CharField(max_length=10, null=True, blank=True)
    room_number = models.CharField(max_length=20, null=True, blank=True)
    type = models.CharField(max_length=20, null=True, blank=True)
    status = models.CharField(max_length=20, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=0)


class Reservation(models.Model):
    MIA_CHOICES = [
        ("m", "M"),
        ("i", "I"),
        ("a", "A"),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, null=False, blank=False)
    group_id = models.CharField(max_length=20, null=True, blank=True)
    room = models.ForeignKey(
        "pms.Room", null=True, related_name="reservations", on_delete=models.SET_NULL
    )
    guest_name = models.CharField(max_length=30, null=True, blank=True)
    check_in_date = models.DateField(null=True, blank=True)
    check_out_date = models.DateField(null=True, blank=True)
    length_of_stay = models.IntegerField(null=True, blank=True)
    services = models.DecimalField(max_digits=10, decimal_places=0)
    total_room_charge = models.DecimalField(max_digits=10, decimal_places=0)
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
    remarks = models.TextField(null=True, blank=True)

    m_i_a = models.CharField(max_length=3, choices=MIA_CHOICES, blank=True, null=True)
    reservation_status = models.CharField(max_length=10, null=True, blank=True)
    room_count = models.IntegerField(null=True, blank=True)
    guest_count = models.IntegerField(null=True, blank=True)
    reservation_path = models.CharField(
        max_length=20, choices=MIA_CHOICES, blank=True, null=True
    )
    vip_guest = models.CharField(
        max_length=20, choices=MIA_CHOICES, blank=True, null=True
    )
    ota_number = models.CharField(
        max_length=20, choices=MIA_CHOICES, blank=True, null=True
    )
    reservation_number = models.CharField(
        max_length=20, choices=MIA_CHOICES, blank=True, null=True
    )
    sales_person = models.CharField(
        max_length=20, choices=MIA_CHOICES, blank=True, null=True
    )
    cancellation_date = models.CharField(
        max_length=20, choices=MIA_CHOICES, blank=True, null=True
    )
    reservation_date = models.CharField(
        max_length=20, choices=MIA_CHOICES, blank=True, null=True
    )
    booker_number = models.CharField(
        max_length=20, choices=MIA_CHOICES, blank=True, null=True
    )
    deposit_number = models.CharField(
        max_length=20, choices=MIA_CHOICES, blank=True, null=True
    )
    deposit_amount = models.DecimalField(max_digits=10, decimal_places=0, null=True)
    vehicle_number = models.CharField(
        max_length=20, choices=MIA_CHOICES, blank=True, null=True
    )
    verifier = models.CharField(
        max_length=20, choices=MIA_CHOICES, blank=True, null=True
    )
    advance_payment = models.DecimalField(
        max_digits=10, decimal_places=0, null=True
    )  # 선수금
    balance_due = models.DecimalField(
        max_digits=10, decimal_places=0, null=True
    )  # 잔액


class CheckInOutStatus(models.Model):
    CHECKINOUT_CHOICES = [
        ("in", "IN"),
        ("out", "OUT"),
    ]

    reservation = models.ForeignKey(
        "pms.Reservation", null=True, related_name="check_in", on_delete=models.SET_NULL
    )
    check_in_time = models.TimeField(null=True, blank=True)
    check_in_out_status = models.CharField(
        max_length=3, choices=CHECKINOUT_CHOICES, blank=True, null=True
    )


class Task(models.Model):
    task_number = models.CharField(max_length=10, null=True, blank=True)
    task_name = models.CharField(max_length=20, null=True, blank=True)
    task_status = models.CharField(max_length=10, null=True, blank=True)
