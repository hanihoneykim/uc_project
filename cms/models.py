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
    integration_status = models.BooleanField(default=False)
    integration_date = models.DateField(null=True, blank=True)
