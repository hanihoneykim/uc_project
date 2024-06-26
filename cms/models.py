from django.db import models


class RatePackage(models.Model):
    room_type = models.CharField(max_length=20, null=True, blank=True)
    lv1d = models.DecimalField(max_digits=10, decimal_places=0)
    lv1t = models.DecimalField(max_digits=10, decimal_places=0)
    lv1f = models.DecimalField(max_digits=10, decimal_places=0)
    lv1s = models.DecimalField(max_digits=10, decimal_places=0)
    lv2d = models.DecimalField(max_digits=10, decimal_places=0)
    lv2t = models.DecimalField(max_digits=10, decimal_places=0)
    lv2f = models.DecimalField(max_digits=10, decimal_places=0)
    lv2s = models.DecimalField(max_digits=10, decimal_places=0)
    lv3d = models.DecimalField(max_digits=10, decimal_places=0)
    lv3t = models.DecimalField(max_digits=10, decimal_places=0)
    lv3f = models.DecimalField(max_digits=10, decimal_places=0)
    lv3s = models.DecimalField(max_digits=10, decimal_places=0)
    lv4d = models.DecimalField(max_digits=10, decimal_places=0)
    lv4t = models.DecimalField(max_digits=10, decimal_places=0)
    lv4f = models.DecimalField(max_digits=10, decimal_places=0)
    lv4s = models.DecimalField(max_digits=10, decimal_places=0)


class Channel(models.Model):
    channel_name = models.CharField(max_length=20, null=True, blank=True)
    integration_status = models.BooleanField(default=False)  # 연동상태
    integration_date = models.DateField(null=True, blank=True)  # 연동일자

    # 더미데이터를 위한 필드 (추후 Reservation model과 연결해 serializer로 계산 구현 예정)
    reservation_count = models.IntegerField(null=True, blank=True)  # 예약수
    length_of_stay = models.IntegerField(null=True, blank=True)  # 숙박일수
    number_of_guests = models.IntegerField(null=True, blank=True)  # 인원수
    revenue = models.DecimalField(max_digits=10, decimal_places=0, default=0)  # 매출
    average_revenue_per_customer = models.DecimalField(
        max_digits=10, decimal_places=0, default=0
    )  # 객단가
    cancellation = models.IntegerField(null=True, blank=True)  # 취소
    no_show = models.IntegerField(null=True, blank=True)  # 노쇼


class CMSReservation(models.Model):
    reservation = models.ForeignKey(
        "pms.Reservation",
        null=True,
        related_name="cms_reservations",
        on_delete=models.SET_NULL,
    )
    channel = models.CharField(max_length=20, null=True, blank=True)
    channel_reservation_number = models.CharField(max_length=20, null=True, blank=True)
    pms_reservation_number = models.CharField(max_length=20, null=True, blank=True)
    pms_status = models.CharField(max_length=20, null=True, blank=True)
    cms_status = models.CharField(max_length=20, null=True, blank=True)
    actual_check_out_date = models.DateField(null=True, blank=True)
    transmission_result = models.BooleanField(default=False)


class History(models.Model):
    user_id = models.CharField(max_length=20, null=True, blank=True)
    user_name = models.CharField(max_length=20, null=True, blank=True)
    connection_date = models.DateTimeField(auto_now=True)
    program_name = models.CharField(max_length=20, null=True, blank=True)
    process = models.CharField(max_length=20, null=True, blank=True)
    process_content = models.CharField(max_length=20, null=True, blank=True)
    user_ip = models.CharField(max_length=20, null=True, blank=True)


class FAQ(models.Model):
    category = models.CharField(max_length=20, null=True, blank=True)
    title = models.CharField(max_length=50, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    link_title = models.CharField(max_length=20, null=True, blank=True)
    link = models.CharField(max_length=50, null=True, blank=True)
