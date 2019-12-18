from django.db import models

import uuid

class Brands(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    brand_name = models.CharField(max_length=100, unique=True)


class Coupons(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    brand = models.ForeignKey(Brands, related_name='brand',on_delete=models.CASCADE)
    coupon_code = models.CharField(max_length=100, unique=True)
    currency_code = models.CharField(max_length=100, default='INR',blank=True)
    denomination = models.IntegerField()
